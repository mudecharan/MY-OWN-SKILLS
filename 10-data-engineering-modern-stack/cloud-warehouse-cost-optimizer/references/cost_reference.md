# Warehouse Cost Optimization Reference

## The audit math that matters
Rank by TOTAL cost, not single-run time:
`cost = avg_runtime × frequency × rate`
A 4-second query running every 60 seconds costs more than a nightly 30-minute monster.
Usually 5–10 query patterns = 60%+ of spend.

## Quick wins (days, not months)
| Fix | Typical effect |
|---|---|
| eliminate SELECT * in scheduled jobs | 20–50% bytes |
| right-size oversized warehouses | 30–70% compute |
| auto-suspend ≤60s | kills idle burn |
| materialize repeated identical queries | near-100% on those queries |
| dashboard refresh storms → event-based or cached | huge when present |

## Workload routing
Separate warehouses per class: ELT / BI / ad-hoc — one team's runaway query
stops starving everyone. Scale OUT for concurrency instead of UP.

## Storage lifecycle
Time Travel retention tuned to actual recovery needs · archive cold partitions to
object storage · drop zombie tables and orphan clones (they silently bill).

## Culture
Per-team cost dashboards with QUERY TAGS for attribution · monthly review ·
celebrate the biggest reduction rather than only shaming the biggest spender.
