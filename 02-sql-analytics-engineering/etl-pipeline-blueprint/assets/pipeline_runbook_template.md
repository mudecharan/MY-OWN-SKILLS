# Pipeline Runbook — <pipeline name>

## Contract
| Item | Value |
|---|---|
| Output table + grain | |
| Freshness SLA (e.g., data available by 07:00 UTC) | |
| Completeness SLA (row count vs trailing 7-day avg) | ±__% |
| Owner / escalation contact | |
| Schedule & dependencies | |

## What runs when
1. <extract job> → raw landing (append-only)
2. <transform> → staging
3. <merge/upsert> → target marts
4. quality checks gate steps 2–3; failure = no publish

## Failure triage order (check in this sequence)
1. **Source down?** — hit the source health endpoint manually.
2. **Schema drift?** — compare last raw payload keys vs contract (`raw_landing/` newest file).
3. **Volume anomaly?** — rows extracted vs 7-day average; partial pagination often halves volume.
4. **Auth expired?** — token refresh logs; re-run credential rotation procedure.
5. **Downstream constraint violation?** — read the exact assert from `quality_checks`.

## Recovery procedures
- Re-run a window: `python incremental_loader.py --start 2024-05-01T00:00:00Z --end 2024-05-02T00:00:00Z` (idempotent).
- Full backfill: loop windows chronologically; throttle to respect source rate limits.

## Monitoring hooks
- [ ] daily smoke test: auth + 1 record per endpoint, before business hours
- [ ] alert on freshness breach at SLA time
- [ ] alert on row-count anomaly (>±40% vs 7-day avg)
