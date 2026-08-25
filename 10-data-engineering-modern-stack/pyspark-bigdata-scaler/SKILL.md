---
name: pyspark-bigdata-scaler
description: Scale pandas-era analysis to big data with Spark — partitioning, shuffles, lazy evaluation, skew fixes, memory tuning. Activate when data exceeds RAM or jobs crawl/OOM.
---

# When to use
- Files/datasets too large for a single machine
- Spark jobs that OOM, spill, or take hours
- Migrating pandas notebooks to cluster-scale

# Process
1. **Mental-model shift** — lazy evaluation, no row loops, transformations build a plan (driver never touches the data); express logic as column operations and window functions.
2. **Partition hygiene** — target 100–200MB partitions; repartition on join/group keys when needed; coalesce before writes; avoid shuffle-inducing distinct/sort without cause.
3. **Skew & spill diagnosis** — read the Spark UI: straggler tasks, spill-to-disk, shuffle read sizes; fix with salting, broadcast joins for small dimensions (auto-broadcast threshold check), AQE enabled.
4. **Join strategy** — broadcast small tables explicitly; bucket/sort tables joined repeatedly; filter + select EARLY (predicate/column pushdown verification via explain plans).
5. **Data layout** — write Parquet partitioned by query-filter columns; Z-order/cluster where supported; compaction of small files as routine maintenance.
6. **Parity testing** — validate scaled pipeline output against pandas results on a sample slice before trusting it.

# Inputs the skill needs
- Required: existing analysis/pipeline, dataset size profile, cluster config
- Optional: cost constraints, upstream scheduling windows

# Output
- Scaled PySpark implementation
- Before/after performance table (runtime, shuffle, spill)
- Partition/layout recommendations embedded as code comments

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/spark_pipeline.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/spark_scaling_reference.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/scaling_report_template.md` - Fill this template - it IS the deliverable format.
