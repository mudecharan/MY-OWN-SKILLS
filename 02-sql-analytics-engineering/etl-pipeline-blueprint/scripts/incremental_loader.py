"""etl-pipeline-blueprint · incremental, idempotent API/file -> warehouse loader skeleton.
Fill the marked hooks. Re-running any date window is safe (idempotent by design).
Requires: requests, pandas, sqlalchemy (or swap load() for your warehouse client).
"""
import hashlib
import json
import time
import logging
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("etl")

STATE_FILE = Path("state.json")          # high-water marks survive restarts
RAW_DIR = Path("raw_landing")            # append-only raw zone


def http_get(url: str, params: dict | None = None, max_retries: int = 5) -> dict:
    """GET with exponential backoff honoring Retry-After and 429/5xx."""
    for attempt in range(1, max_retries + 1):
        resp = requests.get(url, params=params, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code == 429 or resp.status_code >= 500:
            wait = int(resp.headers.get("Retry-After", 2 ** attempt))
            log.warning("HTTP %s — retry %s in %ss", resp.status_code, attempt, wait)
            time.sleep(wait)
            continue
        resp.raise_for_status()
    raise RuntimeError(f"exhausted retries for {url}")


def fetch_window(since_iso: str, until_iso: str) -> list[dict]:
    """HOOK: page through your API between since/until using its cursor style."""
    records, cursor = [], None
    while True:
        params = {"updated_at_gte": since_iso, "updated_at_lt": until_iso}
        if cursor:
            params["cursor"] = cursor
        payload = http_get("https://api.example.com/v1/orders", params=params)  # HOOK endpoint
        batch = payload["data"]                                                  # HOOK shape
        records.extend(batch)
        cursor = payload.get("next_cursor")                                      # HOOK pagination
        if not cursor:
            return records


def transform(records: list[dict]) -> pd.DataFrame:
    """HOOK: normalize JSON nesting to the contracted output schema."""
    df = pd.json_normalize(records)
    df["loaded_at_utc"] = datetime.now(timezone.utc).isoformat()
    return df


def quality_checks(df: pd.DataFrame) -> None:
    """Fail loudly rather than load garbage."""
    assert not df.empty, "empty extract — aborting load"
    assert df["id"].is_unique, "duplicate natural keys post-dedup"
    null_pct = df["amount"].isna().mean()
    assert null_pct < 0.05, f"critical column {null_pct:.0%} null — upstream change?"


def load(df: pd.DataFrame, target_table: str):
    """HOOK: MERGE/upsert on natural key, or delete+insert the loaded windows."""
    log.info("loading %s rows into %s", len(df), target_table)
    # Example (SQLAlchemy): df.to_sql(target_table, engine, if_exists='append')
    df.to_parquet(RAW_DIR / f"{target_table}_{df['loaded_at_utc'].iloc[0][:10]}.parquet")


def run(window_start: str, window_end: str, table: str = "orders"):
    state = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}
    since = window_start or state.get(table, {}).get("high_water_mark", "1970-01-01T00:00:00Z")

    records = fetch_window(since, window_end)
    df = transform(records)
    quality_checks(df)

    RAW_DIR.mkdir(exist_ok=True)
    raw_hash = hashlib.md5(json.dumps(records, default=str).encode()).hexdigest()[:10]
    (RAW_DIR / f"{table}_{raw_hash}.json").write_text(json.dumps(records, default=str))

    load(df.drop_duplicates(subset=["id"], keep="last"), table)              # idempotent dedupe

    new_hwm = max([r.get("updated_at", "") for r in records] or [since])     # advance cursor
    state[table] = {"high_water_mark": new_hwm}
    STATE_FILE.write_text(json.dumps(state, indent=2))
    log.info("done. high-water mark -> %s", new_hwm)


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default=None)
    ap.add_argument("--end", default=datetime.now(timezone.utc).isoformat())
    ap.add_argument("--table", default="orders")
    a = ap.parse_args()
    run(a.start, a.end, a.table)
