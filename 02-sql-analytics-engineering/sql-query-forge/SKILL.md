---
name: sql-query-forge
description: Build production-grade SQL from a business question — correct joins, grain control, edge-case handling, and readable CTE structure. Activate whenever a metric must be computed in SQL.
---

# When to use
- A stakeholder question needs a SQL answer against a warehouse
- Converting a spreadsheet calculation into reliable SQL
- Building the source query behind a dashboard or model

# Process
1. **Restate the question as a spec** — exact metric definition, grain of output rows, time window, filters, and what counts as "a customer/order/event". Get confirmation on ambiguous terms.
2. **Map sources** — identify tables, their grains, join keys, and SCD/type-2 dimensions; note where fan-out could duplicate rows.
3. **Draft in layers** — staged CTEs: `source` → `clean` → `aggregate` → `final`; each CTE does one job with a comment stating its grain.
4. **Edge cases by checklist** — NULLs in join keys, zero-division (NULLIF), late-arriving records, timezone conversion at boundaries, inclusive/exclusive date ranges, duplicate detection via QUALIFY/ROW_NUMBER.
5. **Self-review** — verify row counts at each CTE stage; run sanity totals (e.g., revenue sum matches finance's number within tolerance).
6. **Deliver** — final query + expected-output sample + assumptions block embedded as comments.

# Inputs the skill needs
- Required: business question, target warehouse/dialect (Postgres, Snowflake, BigQuery, etc.)
- Optional: schema docs, known data quirks, performance limits

# Output
- Layered, commented SQL query ready to schedule or share
- Assumptions & definitions block (paste into documentation)
- Sanity-check results proving the numbers reconcile

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/reconcile_metrics.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/sanity_check_pack.sql` - Run against your warehouse (adapt dialect); capture results as evidence.
- `scripts/sql_lint.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/engine_specific_guide.md` - read before executing the Process
- `references/metric_spec_block.md` - read before starting.
- `references/reconciliation_patterns.md` - apply these proven patterns
- `references/sql_pattern_library.md` - read before starting.

### assets/ - templates to fill and deliver
- `assets/layered_query_template.sql` - Adapt and run; paste results into the report template.
- `assets/query_documentation_template.md` - Fill this template - it IS the deliverable format.
- `assets/query_review_template.md` - Fill this template - it IS the deliverable format.
- `assets/reconciliation_report_template.md` - Fill this template - it IS the deliverable format.
