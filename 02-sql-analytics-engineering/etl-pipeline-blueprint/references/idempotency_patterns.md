# Idempotency & Data Quality Patterns for Pipelines

## Idempotency strategies (pick per load type)
| Pattern | When to use |
|---|---|
| Delete+insert by loaded window | date-partitioned facts |
| MERGE/upsert on natural key | slowly changing records with updated_at |
| Append-only + dedup view | event streams where re-ordering happens |

Rule: re-running ANY window twice must yield byte-identical final tables. Test this explicitly.

## Quality gates (fail the pipeline, don't load garbage)
1. Volume: row count within ±X% of trailing 7-day average.
2. Schema: expected columns present, no surprise new columns without review.
3. Nulls: critical columns below threshold.
4. Uniqueness: natural key duplicates = 0 post-dedup.
5. Business invariants: amounts >= 0, dates within extract window.

## Incremental extraction hierarchy (best first)
1. Webhooks / CDC stream
2. updated_at cursor with high-water mark (persist state!)
3. ID-based chunking
4. Full reload (only small tables)

## High-water mark discipline
- Persist AFTER successful load only.
- Overlap windows by a few minutes to catch late commits; dedup handles the rest.
- Clock skew between systems: use SOURCE timestamps, not loader timestamps.

## Schema-drift policy
Unknown new fields: land them in a raw JSON column + alert.
Removed/renamed fields: hard-fail the pipeline — silent NULLs are worse than downtime.
