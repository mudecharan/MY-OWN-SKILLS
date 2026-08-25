---
name: query-performance-doctor
description: Diagnose and fix slow queries using execution plans — index strategy, join reordering, predicate pushdown, partition pruning. Activate when a query times out, costs too much, or blocks dashboards.
---

# When to use
- A dashboard query takes minutes instead of seconds
- Warehouse costs spike and one query is the culprit
- A nightly job overruns its window

# Process
1. **Baseline** — capture runtime, rows scanned, bytes processed, credits consumed (dialect-appropriate EXPLAIN ANALYZE).
2. **Plan reading** — locate the dominant node (full scan, hash join spill, broadcast explosion); identify missing predicates that prevent partition pruning.
3. **Top fixes, cheapest first**:
   - Push filters before joins; select only needed columns
   - Join to pre-aggregated subqueries instead of raw fact tables
   - Fix non-sargable predicates (functions on the indexed column)
   - Recommend clustering keys / indexes / materialized views with cost-benefit math
4. **Rewrite** — produce optimized version; prove equivalence by comparing output checksums/row counts.
5. **Measure** — before/after table: runtime, bytes scanned, cost. Accept only ≥50% improvement or justify stopping.
6. **Prevent** — add the anti-pattern to a team style-guide note.

# Inputs the skill needs
- Required: the slow query, dialect, and access to EXPLAIN output
- Optional: table DDL/indexes, concurrency context, cost ceiling

# Output
- Diagnosis report: bottleneck node, root cause in plain language
- Rewritten query with equivalence proof
- Index/partition/materialization recommendations with estimated impact

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/cardinality_estimator.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/diagnosis_queries.sql` - Run against your warehouse (adapt dialect); capture results as evidence.
- `scripts/explain_plan_parser.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/plan_reading_cheatsheet.md` - keep open while diagnosing
- `references/sql_anti_patterns.md` - apply these proven patterns

### assets/ - templates to fill and deliver
- `assets/diagnosis_report_template.md` - Fill this template - it IS the deliverable format.
- `assets/optimization_recommendations.md` - Fill this template - it IS the deliverable format.
