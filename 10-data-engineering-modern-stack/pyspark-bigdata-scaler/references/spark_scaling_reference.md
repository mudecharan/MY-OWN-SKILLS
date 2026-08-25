# Spark Scaling Reference

## Mental-model shifts from pandas
- Lazy evaluation: transformations build a plan; nothing runs until an action.
- No row loops, no iterrows — everything is column expressions or window functions.
- The driver never holds the data. If you `.collect()`, you've lost.

## Partition hygiene
| Rule | Target |
|---|---|
| partition size | 100–200 MB |
| shuffle partitions | ~2–3× total cores (or AQE auto) |
| before write | coalesce to avoid thousands of tiny files |
| partitionBy on output | the column queries filter on |

## Reading the Spark UI (diagnosis order)
1. Straggler tasks → SKEW: enable AQE skew join, or salt the hot key
2. Spill (memory→disk) → reduce columns/rows earlier, more partitions, bigger executors
3. Huge shuffle read → join strategy wrong: broadcast small side, pre-aggregate
4. Full scan when filter exists → check pushdown in explain plan / file layout

## Join strategies
- Broadcast join for small dims (`F.broadcast`) — kills the biggest shuffles.
- Repeated joins on same keys → bucket/sort tables once.
- Filter and select EARLY; verify with `explain()` that predicates pushed down.

## Storage layout
Parquet always · partitioned by date for time-filtered workloads ·
Z-order/cluster heavy filter columns · schedule small-file compaction as maintenance.

## Migration parity gate
Before trusting a scaled pipeline: run pandas version on a sample slice,
compare outputs (row counts + checksums). Silent logic drift during translation is common.
