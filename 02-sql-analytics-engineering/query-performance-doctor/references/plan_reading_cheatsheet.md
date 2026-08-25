# Plan Reading Cheat Sheet

## What the dominant node tells you
| Symptom in plan | Meaning | First fix |
|---|---|---|
| Full table scan on big table | no partition/index pruning | add sargable filter on cluster key |
| Hash join with huge build side | small-table broadcast failed | lower broadcast threshold or broadcast hint |
| Nested loop over millions | stats stale / wrong join order | analyze/vacuum; force hash join |
| Sort spill to disk | memory too small for sort | reduce columns/rows first, raise warehouse, or pre-sort storage |
| Replication/broadcast explosion | skewed join keys | salting, skew hints, isolate hot keys |
| Distinct/Window high shuffle | dedup late | dedup earlier on smaller projection |

## Sargability rules (predicates that CAN use an index/partition)
- No functions around the indexed column: `where f(col) = x` ❌ → `col between` ✅
- Implicit casts break pruning: `varchar_ts >= DATE '2024-01-01'` may scan everything.
- Leading-column rule for composite indexes: filter must touch the first column.

## Cost math for structural fixes
Index/materialized view pays off when:
`(daily_query_count × seconds_saved × $/sec) > daily_write_overhead`
Estimate both sides before recommending.

## Equivalence testing discipline
Never ship a "faster" query without proving identical output:
row count + checksum (`sum(hash(...))` or `md5(string_agg(...)`) on key metrics.
