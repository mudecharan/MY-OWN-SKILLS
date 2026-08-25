---
name: api-data-ingestor
description: Reliably pull data from REST/GraphQL APIs into analysis-ready storage — pagination, auth, rate limits, incremental sync, schema stability. Activate when the data lives behind an API.
---

# When to use
- SaaS platform data (CRM, ads, payments) needed in your warehouse
- Building recurring extracts from third-party APIs
- Debugging flaky API pulls

# Process
1. **API reconnaissance** — read docs for: pagination style (offset/cursor), rate-limit headers, auth flow (token refresh!), field deprecation policy; test endpoints with minimal calls first.
2. **Respectful client design** — exponential backoff on 429/5xx with Retry-After honor; request only needed fields; batch where supported; concurrency caps.
3. **Incremental strategy** — prefer updated_at cursors or webhooks over full pulls; store high-water marks statefully; plan initial backfill separately from steady-state sync.
4. **Schema resilience** — normalize JSON nesting explicitly; unknown-field tolerance (store raw + parsed); alert on new/removed fields rather than silently breaking.
5. **Idempotent landing** — raw zone append-only with extract timestamps; dedup in transformation layer; re-runnable by date window.
6. **Contract tests** — smoke-test script validating auth + one record per endpoint runs daily before business hours.

# Inputs the skill needs
- Required: API documentation, credentials via secure config
- Optional: quota ceilings, downstream freshness SLAs

# Output
- Working ingestion client (Python) with retry/pagination/incremental logic
- Raw landing schema + parsed view layer
- Monitoring checks and credential rotation notes

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/api_ingest.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/api_ingest_reference.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/ingestion_contract_template.md` - Fill this template - it IS the deliverable format.
