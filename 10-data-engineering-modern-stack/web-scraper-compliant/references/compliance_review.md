# Compliance & Ethics Review (complete BEFORE writing the scraper)

## Gate 1 — Is there a better source? (prefer in this order)
1. Official API / bulk download / data portal
2. Licensed dataset (vendor)
3. Public records / open data
4. Scraping — LAST resort

## Gate 2 — Legal & policy
- [ ] robots.txt checked: are target paths disallowed?
- [ ] Terms of Service reviewed: scraping clauses noted
- [ ] No personal data collected (GDPR/CCPA exposure) — if personal data is unavoidable,
      stop and escalate to legal
- [ ] Copyright: facts fine; reproducing creative content is not

## Gate 3 — Politeness engineering
- [ ] delay ≥1s between requests to same host (default 1.5s)
- [ ] identifiable User-Agent with contact info
- [ ] off-peak scheduling for large crawls
- [ ] caching so pages are never fetched twice
- [ ] concurrency caps; no distributed hammering

## Sign-off record → compliance_signoff.json
```json
{"reviewed": true, "robots_checked": true, "tos_reviewed": true,
 "no_personal_data": true, "date": "", "reviewer": ""}
```

## Engineering notes
- Prefer embedded JSON (script tags / XHR endpoints) over HTML parsing — stabler.
- Store raw HTML beside parsed fields: selectors break, raw doesn't.
- Selector-failure alerts + content-hash change detection = early warning system.
