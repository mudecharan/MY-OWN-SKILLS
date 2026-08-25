"""web-scraper-compliant · polite, resilient page scraper with structure-change alarms.
Usage: python scraper.py --urls urls.txt --fields "title:h1,price:.price::text"
BEFORE running: complete the compliance review (see references/compliance_review.md).
"""
import argparse
import hashlib
import json
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

RAW = Path("raw_html")
STATE = Path("scraper_state.json")


def compliance_gate():
    """Hard gate — the script refuses to run without a recorded review."""
    ok_path = Path("compliance_signoff.json")
    if not ok_path.exists():
        raise SystemExit(
            "COMPLIANCE REVIEW MISSING. Complete references/compliance_review.md,\n"
            "then write {\"reviewed\": true, \"robots_checked\": true, \"tos_reviewed\": true,\n"
            " \"date\": \"...\", \"reviewer\": \"...\"} to compliance_signoff.json")
    print("Compliance sign-off found:", json.loads(ok_path.read_text()))


def fetch(url, session):
    r = session.get(url, timeout=20,
                    headers={"User-Agent": "research-bot (+contact: you@example.com)"})
    r.raise_for_status()
    return r.text


def parse(html: str, fields: dict) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    out = {}
    for name, sel in fields.items():
        if "::text" in sel:
            css = sel.replace("::text", "")
            node = soup.select_one(css)
            out[name] = node.get_text(strip=True) if node else None
        elif ":" in sel and not sel.startswith((".", "#", "h", "div", "span")):
            tag, attr = sel.split(":", 1)
            node = soup.select_one(tag)
            out[name] = node.get(attr) if node else None
        else:
            node = soup.select_one(sel)
            out[name] = node.get_text(strip=True) if node else None
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--urls", required=True)
    ap.add_argument("--fields", required=True, help='name:css_selector[,name:selector...]')
    ap.add_argument("--delay", type=float, default=1.5, help="politeness delay seconds")
    args = ap.parse_args()

    compliance_gate()
    fields = dict(f.split(":", 1) for f in args.fields.split(","))
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    RAW.mkdir(exist_ok=True)
    rows, broken_selectors = [], set()

    with requests.Session() as s:
        for url in [u.strip() for u in Path(args.urls).read_text().splitlines() if u.strip()]:
            h = hashlib.md5(url.encode()).hexdigest()[:12]
            try:
                html = fetch(url, s)
                (RAW / f"{h}.html").write_text(html, encoding="utf-8")

                # change detection: skip parse if unchanged
                digest = hashlib.md5(html.encode()).hexdigest()
                if state.get(url) == digest:
                    continue
                row = {"url": url}
                row.update(parse(html, fields))
                for k, v in row.items():
                    if v is None and k != "url":
                        broken_selectors.add(k)
                row["scraped_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
                rows.append(row)
                state[url] = digest
            except Exception as e:
                print(f"FAIL {url}: {e}")
            time.sleep(args.delay)

    STATE.write_text(json.dumps(state, indent=2))
    import pandas as pd
    df = pd.DataFrame(rows).drop_duplicates(subset=["url"])
    out = f"scraped_{time.strftime('%Y%m%d')}.parquet"
    df.to_parquet(out)
    print(f"saved {len(df)} rows -> {out}")
    if broken_selectors:
        print(f"⚠ SELECTOR ALERT — fields returning None (site structure changed?): {broken_selectors}")


if __name__ == "__main__":
    main()
