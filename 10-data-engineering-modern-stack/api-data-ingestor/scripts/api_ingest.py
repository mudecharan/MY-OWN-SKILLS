"""api-data-ingestor · paginated API client with backoff + incremental cursor sync.
Usage: python api_ingest.py --endpoint https://api.example.com/v1/events [--since 2024-05-01T00:00:00Z]
Adapt the marked HOOKS to your API's pagination/field names. State survives restarts.
"""
import argparse
import json
import time
from pathlib import Path

import pandas as pd
import requests

STATE = Path("ingest_state.json")


def get(url, params, headers=None, max_retries=6):
    for attempt in range(1, max_retries + 1):
        r = requests.get(url, params=params, headers=headers, timeout=30)
        if r.status_code == 200:
            return r.json()
        if r.status_code in (429,) or r.status_code >= 500:
            wait = int(r.headers.get("Retry-After", min(60, 2 ** attempt)))
            print(f"HTTP {r.status_code}: retry {attempt}/{max_retries} in {wait}s")
            time.sleep(wait)
            continue
        r.raise_for_status()
    raise RuntimeError(f"retries exhausted: {url}")


def fetch_all(endpoint, since, until):
    """HOOK: match your API's cursor/offset style."""
    out, cursor = [], None
    while True:
        params = {"updated_at_gte": since, "updated_at_lt": until}
        if cursor:
            params["page[cursor]"] = cursor                      # HOOK param name
        data = get(endpoint, params)                              # add auth headers
        batch = data.get("data", [])                              # HOOK payload key
        out.extend(batch)
        cursor = (data.get("meta") or {}).get("next_cursor")      # HOOK pagination
        if not cursor or not batch:
            return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--endpoint", required=True)
    ap.add_argument("--since", default=None)
    ap.add_argument("--until")
    ap.add_argument("--out-prefix", default="api_extract")
    a = ap.parse_args()

    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    since = a.since or state.get(a.endpoint, {}).get("hwm", "1970-01-01T00:00:00Z")
    until = a.until or pd.Timestamp.utcnow().isoformat()

    records = fetch_all(a.endpoint, since, until)
    df = pd.json_normalize(records)

    # quality gates — fail loudly rather than load garbage
    assert records, "empty extract; check cursor/window"
    if "id" in df.columns:
        dupes = df["id"].duplicated().sum()
        print(f"rows={len(df):,} duplicate ids post-fetch={dupes} "
              f"{'(dedupe on load)' if dupes else ''}")

    raw_name = f"{a.out_prefix}_{pd.Timestamp.utcnow():%Y%m%d%H%M%S}.json"
    Path(raw_name).write_text(json.dumps(records, default=str))
    df.to_parquet(raw_name.replace(".json", ".parquet"))
    print(f"landed -> {raw_name}.parquet")

    hwm = max([r.get("updated_at", "") for r in records] + [since])   # HOOK field name
    state[a.endpoint] = {"hwm": hwm}
    STATE.write_text(json.dumps(state, indent=2))
    print(f"high-water mark -> {hwm}")
