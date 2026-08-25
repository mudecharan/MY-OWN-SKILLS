---
name: web-scraper-compliant
description: Extract public web data legally and robustly — robots.txt compliance, anti-bot navigation, structure parsing, change-resilient selectors. Activate when needed data exists only on web pages.
---

# When to use
- Competitor pricing/catalog monitoring
- Public records aggregation (listings, filings, events)
- No API alternative exists

# Process
1. **Legality & ethics gate FIRST** — robots.txt, terms of service, rate limiting courtesy (≥1 req/sec), personal-data avoidance (GDPR), prefer official APIs/bulk downloads whenever they exist. Document this review — it's part of the deliverable.
2. **Structure reconnaissance** — inspect DOM, identify stable anchors (semantic attributes > positional indexes); check for embedded JSON (script tags/API XHR calls) which beats HTML parsing every time.
3. **Resilient extraction** — CSS/XPath selectors with fallbacks; schema validation per page (missing fields = structural change alarm); store raw HTML alongside parsed data for re-parsing.
4. **Scale politely** — async/concurrent fetching within politeness limits, session rotation only if legitimately required, caching to never fetch twice.
5. **Change detection** — selector-failure alerts, content-hash diffing to skip unchanged pages.
6. **Output hygiene** — dedupe across runs, timestamp every record (web data is point-in-time), provenance URL column.

# Inputs the skill needs
- Required: target URLs/sites, fields wanted
- Optional: refresh frequency, historical snapshots

# Output
- Working scraper with compliance review documented
- Parsed, deduped dataset with provenance and timestamps
- Monitoring for site-structure breakage

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/scraper.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/compliance_review.md` - read before starting.

### assets/ - templates to fill and deliver
- `assets/dataset_doc_template.md` - Fill this template - it IS the deliverable format.
