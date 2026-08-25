---
name: data
description: Comprehensive Data Analytics Skills suite. 31 reusable analytical skills across 6 categories — data quality & validation, documentation & knowledge, data analysis & investigation, data storytelling & visualization, stakeholder communication, and workflow optimization. Activate on-demand for any data analysis task including EDA, SQL review, cohort/segmentation/funnel/time-series analysis, A/B testing, dashboards, executive summaries, and more.
---

# Data Analytics Skills Suite

A library of 31 reusable analytical skills organized into 6 categories. Each skill follows an on-demand context pattern: request minimum viable context, execute a structured workflow, surface assumptions, and deliver a consistent output. Skills degrade gracefully — if you can't provide everything, state what you're assuming and proceed.

## How to Use These Skills

Describe your task naturally — the right skill will activate automatically. Each skill requests the specific context it needs, follows a structured workflow with checkpoints, and produces consistent high-quality outputs.

**Common trigger pattern:**

```
You:    "I need to understand why our activation rate dropped 12% last week"
Agent:  [activates root-cause-investigation, asks for metric data and context]
You:    [provides data and business context]
Agent:  [runs structured investigation with hypothesis testing]
```

### Which skill to start with?

| You need to... | Start here |
|---------------|-----------|
| Explore an unfamiliar dataset | `programmatic-eda` → `data-quality-audit` |
| Write or review SQL | `query-validation` + `schema-mapper` |
| Understand a metric drop/spike | `root-cause-investigation` |
| Analyze experiment results | `ab-test-analysis` |
| Build a dashboard | `dashboard-specification` + `visualization-builder` |
| Present to leadership | `executive-summary-generator` + `insight-synthesis` |
| Document your methodology | `analysis-documentation` + `analysis-assumptions-log` |
| Start a complex analysis | `analysis-planning` first, always |

### Pro Tips
- **Prepare context in advance**: schema, key tables, key metrics, business rules
- **Chain skills together**: e.g., programmatic-eda → cohort-analysis → insight-synthesis → executive-summary-generator
- **Iterate progressively**: start basic, dive deeper where you see patterns, refine
- **Use checkpoints**: confirm understanding before execution, review intermediate findings, adjust direction

---

## Category 01 · Data Quality & Validation (5 skills)

*Foundation — start here whenever you're working with new data.*

### 1. programmatic-eda

**Systematic exploratory data analysis. Activate when a dataset needs profiling — structure check, nulls, outliers, distributions, correlations — before deeper analysis begins.**

**When to use**
- You receive a new dataset and need to understand its shape and quality before analysis
- An analysis produces surprising numbers and you want to verify the underlying data first
- A stakeholder asks "is this data reliable?" or "what's in this table?"
- You're about to run a model or statistical test and need data-quality assurance

**Process**
1. **Load and overview** — run `scripts/data_overview.py` to get row count, dtypes, memory usage, and a sample. Confirm grain (what one row represents).
2. **Null profile** — run `scripts/null_profiler.py`; compare output against thresholds in `references/quality_thresholds.md` and flag columns above limits.
3. **Outlier detection** — run `scripts/outlier_detector.py` (IQR + z-score) on numeric columns; document flagged values and decide: real signal or data error?
4. **Distribution summary** — run `scripts/distribution_summary.py` for descriptive stats and univariate histograms on each numeric column.
5. **Correlation exploration** — run `scripts/correlation_explorer.py`; flag pairs with |r| > 0.8 as potential multicollinearity or redundancy.
6. **EDA checklist sign-off** — work through `references/eda_checklist.md` and confirm each item before declaring the dataset profiled.
7. **Write findings** — fill `assets/eda_report_template.md` with full profiling output; distil top issues into `assets/findings_summary.md`.

**Inputs the skill needs**
- Required: dataset path (CSV / Parquet / Excel) or a DataFrame already in scope
- Required: business context — what does one row represent?
- Optional: quality threshold overrides (defaults in `references/quality_thresholds.md`)
- Optional: columns to skip (PII, binary blobs, high-cardinality IDs)

**Output**
- `assets/eda_report_template.md` (filled) — full profiling report with per-column stats
- `assets/findings_summary.md` (filled) — top 3–5 quality issues and recommended next steps
- Console output / plots from scripts for interactive inspection

---

### 2. data-quality-audit

**Comprehensive data quality assessment against business rules, schema constraints, and freshness expectations. Activate when validating data pipeline outputs before production use, auditing a dataset against defined business rules, or producing a quality scorecard for a data asset.**

**When to use**
- A data pipeline has just loaded new data and needs validation before downstream reports consume it
- A stakeholder has flagged data quality concerns (wrong totals, unexpected nulls, stale data)
- You need to produce a formal data quality scorecard for a data asset as part of a data governance process
- You are onboarding a new data source and need to understand its quality profile before building on it

**Process**
1. **Null and completeness audit** — run `scripts/null_counter.py` for a column-by-column null profile. Flag columns above acceptable thresholds for the business context.
2. **Duplicate detection** — run `scripts/duplicate_finder.py` to identify full-row and key-level duplicates. Determine if duplicates are intentional (versioning) or errors (pipeline fan-out).
3. **Referential integrity check** — run `scripts/referential_integrity.py` to validate that foreign key values in child tables exist in parent tables. Report orphan rate per relationship.
4. **Value range validation** — run `scripts/value_range_validator.py` with business rules defined in `references/business_rule_patterns.md`. Flag values outside acceptable ranges.
5. **Freshness check** — run `scripts/freshness_check.py` to verify the dataset is up to date — compare the latest record timestamp against the expected lag for this pipeline.
6. **Score and classify findings** — map each finding to a quality dimension using `references/quality_dimensions.md`. Assign severity (CRITICAL / HIGH / MEDIUM / LOW).
7. **Produce deliverables** — fill `assets/audit_report_template.html` for a shareable report; fill `assets/quality_rubric.md` for a concise scorecard.

**Inputs the skill needs**
- Required: dataset (CSV / Parquet / database table reference)
- Required: schema relationships — which columns are primary keys, which are foreign keys to which tables
- Required: business rules — acceptable value ranges, expected value sets, freshness SLA
- Optional: acceptable error rates — at what threshold does a failure become CRITICAL vs. HIGH
- Optional: pipeline schedule — to assess freshness relative to expected update frequency

**Output**
- `assets/audit_report_template.html` (filled) — full quality report, shareable with stakeholders
- `assets/quality_rubric.md` (filled) — one-page quality scorecard with dimension scores
- Script console output — per-check pass/fail counts for each validation script

---

### 3. query-validation

**SQL query review for correctness, performance, and best practices. Activate when a query needs review before production use, shows unexpected results, or runs too slowly.**

**When to use**
- A SQL query is about to be promoted to a production dashboard or report
- A query is returning surprising or incorrect results
- A query is running slowly and needs performance review
- You want to catch anti-patterns (implicit conversions, SELECT *, unbounded CTEs) before they cause incidents

**Process**
1. **Lint the query** — run `scripts/sql_lint.py` (sqlglot-based) to catch syntax errors, unsupported functions for the target engine, and style violations. Fix hard errors before continuing.
2. **Review anti-patterns** — compare the query structure against `references/sql_anti_patterns.md`. Flag any present anti-patterns with a severity rating.
3. **Parse the explain plan** — if an EXPLAIN or query profile output is available, run `scripts/explain_plan_parser.py` to extract slow steps (full table scans, missing indexes, high row estimates).
4. **Estimate cardinality** — run `scripts/cardinality_estimator.py` if schema stats are available to flag joins that might fan-out unexpectedly.
5. **Check engine-specific behaviour** — consult `references/engine_specific_guide.md` for the target engine (Snowflake / BigQuery / Postgres / Redshift) to verify date functions, window behaviour, and clustering assumptions.
6. **Produce review output** — fill in `assets/query_review_template.md` with findings; for any performance issues found, complete `assets/optimization_recommendations.md`.

**Inputs the skill needs**
- Required: the SQL query text
- Required: target database engine (Snowflake / BigQuery / Postgres / Redshift / other)
- Optional: relevant table schemas (column names, types, approximate row counts)
- Optional: EXPLAIN / query profile output
- Optional: expected business logic — what should the query calculate?

**Output**
- `assets/query_review_template.md` (filled) — categorised findings: correctness, performance, style
- `assets/optimization_recommendations.md` (filled, if issues found) — ranked rewrite suggestions with expected impact

---

### 4. schema-mapper

**Database schema understanding and relationship mapping. Use when exploring unfamiliar databases, documenting table relationships, identifying join paths, or generating ERD documentation for existing schemas.**

**Quick Start**
Automatically discover, document, and visualize database schemas including tables, columns, relationships, and join paths. Essential for understanding unfamiliar databases or creating documentation.

**Context Requirements**
1. **Database Access**: Connection details or schema export
2. **Scope**: Which tables/schemas to map (or all)
3. **Documentation Goal**: What you need (ERD, join paths, data dictionary, etc.)
4. **Known Relationships** (optional): Explicit foreign keys or implicit relationships

**Workflow**
1. **Connect and discover schema** — inspect available schemas and tables. Checkpoint: "Found {N} tables in schema. Does this look right?"
2. **Extract table metadata** — columns, primary keys, foreign keys, indexes, unique constraints for each table.
3. **Infer relationships** — from explicit foreign keys + column naming patterns (`user_id` → `users.id`), with confidence levels (high/medium).
4. **Generate data dictionary** — table × column catalogue with type, nullable, default, PK/FK flags.
5. **Find join paths** — BFS shortest path between any two tables (e.g., orders → customers), producing exact JOIN SQL.
6. **Generate ERD** — Mermaid `erDiagram` output showing tables with PK/FK columns and relationships.
7. **Generate quick reference guide** — table overview, primary keys, and common join patterns in SQL.

**Context Validation** — verify: connection works, target tables defined, INFORMATION_SCHEMA permissions, explicit vs inferred relationships understood, documentation format known.

**Common Scenarios**
- "New to the database, need overview" → full schema map with ERD and data dictionary
- "How do I join Table A to Table B?" → find_join_path with exact SQL, multi-hop joins
- "Document schema for new team members" → comprehensive quick reference + visual ERD
- "Find all tables related to users" → traverse relationship graph, direct and indirect
- "Validate schema against expectations" → compare actual vs documented schema, flag drift

**Handling Missing Context**
- No context → map entire schema and present overview, then drill into areas of interest
- Read-only access → use INFORMATION_SCHEMA queries (structure, not data samples)
- dbt project → extract schema from models and docs (often better business context)
- FKs not enforced → infer from naming patterns, review 'inferred' relationships

**Advanced Options**
- Lineage tracking (raw → transforms → fact tables)
- Schema comparison (dev vs prod, over time)
- Query pattern analysis from logs
- dbt `schema.yml` generation
- Auto-documentation on schema changes
- Performance insights from table sizes and join patterns

**Output**
- `schema_erd.mmd` (Mermaid ERD)
- `data_dictionary.csv` (All columns)
- `schema_quick_reference.md` (Join guide)
- `relationship_graph.json` (Machine-readable)

---

### 5. metric-reconciliation

**Cross-source metric validation and discrepancy investigation. Use when metrics from different sources don't match, investigating data quality issues between systems, or validating data migration accuracy.**

**Quick Start**
Systematically compare metrics across different data sources, identify discrepancies, investigate root causes, and produce reconciliation reports with actionable fixes.

**Context Requirements**
1. **Data Sources**: The 2+ systems/datasets to compare
2. **Metric Definitions**: How each source calculates the metric
3. **Expected Variance**: What difference is acceptable vs. concerning
4. **Time Period**: What date range to reconcile
5. **Join Keys**: How to match records across sources

**Context Gathering**
- For each source: connection details OR CSV export OR SQL query, system name, which metric
- Metric definitions: calculation logic per source, known differences (refunds, transaction types, time zones, granularity)
- Expected variance thresholds: financial <0.1%, user metrics <2%, behavioral <5%; trigger investigation levels
- Time period: specific dates, last N days, relative period, or all time
- Join strategies: aggregate comparison, time-based, entity-based, multi-key comparison

**Workflow**
1. **Load data from each source** — validate record counts look reasonable.
2. **Standardize data formats** — convert dates/metrics, drop nulls, add source identifiers.
3. **Aggregate at comparison level** — group by date (or chosen join key).
4. **Join and compare** — full outer join; compute difference, absolute difference, % difference.
5. **Analyze discrepancies** — categorize as MATCH / MINOR / SIGNIFICANT vs threshold; summary statistics.
6. **Investigate root causes** — top discrepancies, variance trend (improving/worsening), systematic bias, worst day-of-week.
7. **Drill down on specific discrepancies** — transaction-level comparison; find missing/extra records by ID.
8. **Generate reconciliation report** — summary, top discrepancies, root cause analysis, recommendations; save CSV exports.

**Context Validation** — verify: access to all sources, metric definitions clear, variance thresholds known, time periods aligned, unique identifiers available.

**Common Scenarios**
- "Daily revenue doesn't match between systems" → compare daily aggregates, drill into specific days
- "Migration validation" → compare overlapping periods, match by ID, validate calculation logic
- "Financial reconciliation for month-end" → strict threshold (<0.1%), investigate every discrepancy
- "Dashboard vs report numbers differ" → compare underlying queries, identify filter/timing differences
- "Quarterly KPI validation" → reconcile multiple metrics, prioritize fixes by business impact

**Handling Missing Context**
- No specifics → ask for metric, the two numbers, sources, time period
- Unknown definitions → extract underlying queries, reverse-engineer calculations
- No direct data access → work with CSV exports or summary screenshots
- No transaction-level data → aggregate comparison only, note limitations

**Advanced Options**
- Automated daily reconciliation with alerts
- Multi-source reconciliation matrix (3+ sources)
- Trend analysis of reconciliation quality over time
- Root cause classification (timing lag, missing data, calculation difference)
- Formal documentation of known source differences

**Output**
- `reconciliation_report.txt` — full report with summary, top discrepancies, root cause analysis
- `detailed_comparison.csv` — daily breakdown
- `discrepancies_only.csv` — issues for investigation

---

## Category 02 · Documentation & Knowledge (5 skills)

*Build reusable context so you never explain the same thing twice.*

### 6. semantic-model-builder

**Build structured semantic layer documentation for metrics, dimensions, and entities. Activate when you need to define a business metric, document a data model, or create YAML definitions compatible with dbt Semantic Layer or similar frameworks.**

**When to use**
- A stakeholder asks "how is [metric] calculated?" and no canonical definition exists
- You're setting up dbt Semantic Layer and need YAML metric/dimension/entity definitions
- Multiple teams are using different SQL queries for the same metric — you need to codify the one true definition
- You're building a data catalog entry for a core model and need structured metadata

**Process**
1. **Identify the object type** — decide whether you're documenting a metric, a dimension, or an entity. Use the frameworks in `references/metric_definition_framework.md` for metrics and `references/dimension_hierarchy_patterns.md` for dimensions.
2. **Gather the definition inputs** — collect: calculation logic (SQL or formula), business context, data source(s), grain, edge cases, and known gotchas. Ask the data owner if anything is unclear.
3. **Generate the YAML template** — run `scripts/metric_template_generator.py` to scaffold the initial YAML structure for the object type. Fill in the generated template.
4. **Validate the YAML** — run `scripts/model_yaml_validator.py` to check required fields, type constraints, and reference integrity (referenced dimensions exist in the same file).
5. **Add dbt context** — if this will be deployed to dbt Semantic Layer, consult `references/dbt_semantic_layer_guide.md` for the exact field names and constraints for your dbt version.
6. **Save final definitions** — save metrics to `assets/metric_definition.yaml`, dimensions to `assets/dimension_definition.yaml`, entities to `assets/entity_definition.yaml`.

**Inputs the skill needs**
- Required: the metric name or model name to document
- Required: calculation logic — SQL snippet, formula, or plain-English steps
- Required: business context — who uses it, what decision it informs, what a "good" value looks like
- Optional: data source table(s) and column names
- Optional: target semantic layer framework (dbt Semantic Layer, Cube.js, LookML, etc.)
- Optional: existing YAML to validate

**Output**
- `assets/metric_definition.yaml` — filled metric YAML definition(s)
- `assets/dimension_definition.yaml` — filled dimension YAML definition(s)
- `assets/entity_definition.yaml` — filled entity YAML definition(s)
- Validation report from `scripts/model_yaml_validator.py` (inline output)

---

### 7. analysis-documentation

**Structured, reproducible analysis documentation. Use when documenting analysis findings, creating analysis notebooks, ensuring reproducibility, or building analysis archives for future reference.**

**When to use**
- Finalising an analysis before sharing it with stakeholders
- Handing off an analysis to another team member or to a future self
- Archiving recurring analyses so they can be run again consistently
- Preparing for peer review or a formal audit
- Converting an exploratory notebook into a reference document

**Process**
1. **Confirm audience and scope** — determine whether the primary reader is technical (data team), business (stakeholders), or both. For mixed audiences, use a tiered structure. See `references/audience_depth_guide.md` for calibration.
2. **Write the business context section** — state the business question, the stakeholders who requested the analysis, the decisions it informs, and the success criteria.
3. **Document data sources** — for each source, record the table or file, date range, row count, key columns, and any known quality issues or exclusions applied.
4. **Write the methodology section** — describe the analytical approach, tools and library versions, key assumptions, and important decisions made (and alternatives considered). Reference the assumptions log if one exists.
5. **Record results** — include key metrics and statistics, embed or link visualisations with descriptive captions, and present findings in order of importance.
6. **Write the insights, recommendations, and reproducibility section** — connect each finding to a business implication and a next action. Document the steps required to reproduce the analysis (data access, environment, execution order). Use `assets/analysis_doc_template.md` as the structure.

**Inputs the skill needs**
- Final code (SQL, Python, notebook) and outputs (charts, tables)
- Business question and stakeholder context
- Key findings and recommendations already identified
- Data source details (tables, date ranges, sample sizes)
- Library and tool versions used

**Output**
- `assets/analysis_doc_template.md` — completed analysis document covering context, data, methodology, results, and reproducibility
- Linked or embedded visualisations and code references

---

### 8. data-catalog-entry

**Create standardized metadata for data assets. Use when documenting new datasets, building data catalogs, improving data discoverability, or creating data dictionaries for teams.**

**When to use**
- A new table, view, or dataset has been created and needs to be discoverable
- Analysts keep asking the same questions about a table's meaning or ownership
- A compliance or audit requirement mandates documentation of sensitive data
- Onboarding new team members who need to understand available data assets
- Auditing catalog completeness to find undocumented tables

**Process**
1. **Extract technical metadata** — pull schema, column names, types, primary keys, foreign keys, and row count from `INFORMATION_SCHEMA` or the source system. Use `scripts/catalog_extractor.py` to automate this for database tables.
2. **Collect business context** — interview the data owner to capture the business purpose, owning team, criticality (critical / high / medium / low), and known use cases. Record the business-friendly display name.
3. **Write column descriptions** — for each column, write a one-sentence plain-language description, note example values, and document any business rules (valid values, constraints, format requirements).
4. **Assess data quality** — calculate or estimate completeness, freshness (hours since last update), and duplicate rate. Document known issues and how they affect downstream use.
5. **Document lineage** — record upstream sources (where the data comes from) and downstream consumers (dashboards, models, reports that depend on it).
6. **Add governance details and publish** — specify access level (public/restricted/confidential), sensitivity (PII, financial, health), compliance tags, retention policy, and access instructions. Complete `assets/catalog_entry_template.md` and submit to the catalog.

**Inputs the skill needs**
- Connection or export from the database/source system for technical metadata
- Data owner contact for business context interview
- Knowledge of upstream sources and downstream consumers
- Applicable governance policies (PII classification, retention rules)
- Any existing partial documentation or data dictionary

**Output**
- `scripts/catalog_extractor.py` — extracts schema and basic stats from a database table
- `assets/catalog_entry_template.md` — completed catalog entry with technical, business, quality, lineage, and governance sections

---

### 9. sql-to-business-logic

**Translate SQL queries into plain language business logic. Use when documenting queries, explaining analysis to non-technical stakeholders, code reviewing for correctness, or building a query catalog.**

**When to use**
- A stakeholder asks "what exactly does this query calculate?"
- Documenting a query library or a dbt model for non-technical readers
- Reviewing a query for correctness by comparing its logic to the business requirement
- Onboarding new analysts to existing SQL patterns
- Translating legacy undocumented queries before refactoring

**Process**
1. **Receive the query and context** — obtain the SQL and the business question it answers. Also collect any schema notes (what the key tables and columns represent in business terms).
2. **Translate the FROM/JOIN structure** — describe in plain language which data sources are combined and what type of join is used (inner keeps only matches; left keeps all rows from the left side). Note if the join type seems inconsistent with the stated purpose.
3. **Translate WHERE filters** — list each filter condition as a business rule in plain language (e.g., `status = 'completed'` → "only includes orders that have been paid and fulfilled").
4. **Explain GROUP BY and aggregations** — describe what each aggregation computes and at what grain. Use `scripts/sql_explainer.py` to automate a first-pass structural parse.
5. **Summarise output columns** — for each output column, state its business meaning and any edge cases (nulls, rounding, currency units).
6. **Flag issues and write validation questions** — identify potential problems (implicit null propagation, unexpected fan-out, hardcoded dates). Generate 3–5 questions the query author should confirm. Use `assets/query_documentation_template.md` to record the full translation.

**Inputs the skill needs**
- The complete SQL query (SELECT through ORDER BY)
- The business question the query is intended to answer
- Table and column descriptions (or a data catalog entry)
- Any business rules for key status values, date handling, or currency
- The intended output: who reads the result and for what decision

**Output**
- `scripts/sql_explainer.py` — parses a SQL query and generates a structured plain-language explanation
- `assets/query_documentation_template.md` — completed translation covering purpose, step-by-step logic, output columns, business rules, and validation questions
- Optionally: a flowchart representation of the query logic

---

### 10. analysis-assumptions-log

**Track and document analytical assumptions and decisions. Use when making analytical choices, documenting trade-offs, ensuring transparency, or creating audit trails for analytical work.**

**When to use**
- Starting an analysis with significant scope, method, or data quality choices
- Preparing work for peer review or stakeholder sign-off
- Returning to an old analysis and needing to understand prior decisions
- Working in a regulated environment where auditability is required
- Handing off an analysis to another analyst

**Process**
1. **Initialize the log** — create a log entry for the analysis with its name, date, analyst, and the decision it informs. Use `scripts/assumptions_tracker.py` to initialise a structured JSON log.
2. **Enumerate data assumptions** — document representativeness, completeness, how missing values are handled, and any known quality issues. For each assumption, record the rationale and confidence level (high/medium/low). See `references/assumption_categories.md` for the full taxonomy.
3. **Enumerate business logic assumptions** — record metric definitions, time windows, inclusion/exclusion rules, and any definitions provided by stakeholders. Note alternatives considered.
4. **Enumerate statistical assumptions** — record distribution assumptions, independence claims, stationarity, or model assumptions relevant to the methods used.
5. **Assess impact and flag critical assumptions** — for each low-confidence assumption with high impact if wrong, create a validation plan. Run `scripts/assumptions_tracker.py --report` to surface the critical list.
6. **Validate and close** — as validation occurs, update the log with results. Export `assets/assumptions_log_template.md` for peer review sign-off before delivery.

**Inputs the skill needs**
- Analysis name and the decision it informs
- Data sources, time period, and population being analysed
- Key methodological choices made (and alternatives considered)
- Stakeholder-provided business rule definitions
- Any known data quality issues

**Output**
- `scripts/assumptions_tracker.py` — CLI tool to log assumptions, flag critical ones, and export a summary
- `assets/assumptions_log_template.md` — completed log for peer review and audit trail

---

## Category 03 · Data Analysis & Investigation (7 skills)

*Core workflows for the analytical heavy lifting.*

### 11. cohort-analysis

**Time-based cohort analysis with retention and behaviour tracking. Activate when you need to measure how groups of users/customers behave over time — retention rates, revenue by cohort, or feature adoption curves.**

**When to use**
- A stakeholder asks "are we retaining users better than last quarter?"
- You need to measure N-day, weekly, or monthly retention for a product or feature
- You want to compare how different acquisition cohorts (by channel, plan, or signup date) perform over their lifetime
- You're investigating churn and need to identify at which period users typically leave

**Process**
1. **Define the cohort and activity** — clarify: cohort grouping (signup month, first purchase date, etc.) and retention event (login, purchase, feature use). Document in the report header.
2. **Pull or build the data** — if starting from a database, use `scripts/cohort_query.sql` as the starting point. Adapt the `cohort_date` and `activity_date` columns to your schema.
3. **Build the cohort table** — run `scripts/cohort_builder.py` to produce a cohort × period membership table from event data. Output is a CSV with `user_id`, `cohort_period`, `activity_period`.
4. **Compute the retention matrix** — run `scripts/retention_matrix.py` on the cohort table to generate the period-over-period retention rates. Output is an N×M matrix (cohort × period).
5. **Visualise** — run `scripts/cohort_visualizer.py` to render a heatmap of the retention matrix and a time-series of retention curves per cohort.
6. **Interpret findings** — consult `references/retention_metrics_glossary.md` for metric definitions and `references/cohort_definition_patterns.md` for pattern recognition.
7. **Write the report** — fill `assets/cohort_report_template.md`. For a visual deliverable, fill in the `assets/retention_matrix.html` heatmap template.

**Inputs the skill needs**
- Required: event data with `user_id`, `cohort_date` (e.g. `signup_date`), `activity_date`
- Required: cohort grouping granularity (daily / weekly / monthly)
- Required: retention event definition — what counts as "active" or "retained"?
- Optional: minimum cohort size (recommend ≥ 100 users; smaller cohorts have noisy rates)
- Optional: number of periods to track (e.g. 12 months)
- Optional: cohort attributes to segment by (acquisition channel, plan tier, geography)

**Output**
- `assets/cohort_report_template.md` (filled) — narrative interpretation and retention figures
- `assets/retention_matrix.html` (filled) — colour-coded retention heatmap
- `scripts/retention_matrix.py` output CSV — raw retention rates for downstream use

---

### 12. segmentation-analysis

**Customer/user segmentation with actionable insights. Use when identifying distinct customer groups, analyzing segment-specific behavior, profiling high-value segments, or testing segmentation hypotheses.**

**When to use**
- The team needs to understand who the best customers are and what distinguishes them
- Marketing wants distinct groups to target with different messages or offers
- Product needs to prioritise features based on high-value user behaviour patterns
- Churn is high and the team needs to identify at-risk users before they leave
- An existing segmentation feels arbitrary and needs data validation or improvement

**Process**
1. **Define the segmentation goal** — clarify what decisions the segments will inform (product roadmap, marketing campaigns, retention programs). The goal determines which variables matter and how many segments are useful (typically 3–7). See `references/segmentation_approaches.md`.
2. **Select and prepare variables** — choose 3–7 attributes or behaviours that vary across users and relate to the business outcome. Handle missing values and scale continuous variables. Remove outliers only if they would distort cluster centroids.
3. **Run the segmentation** — for data-driven segmentation, use k-means clustering via `scripts/segmentation_runner.py`. For rule-based segmentation, apply the business logic rules and validate that segments are distinct and non-overlapping.
4. **Profile each segment** — compute the mean and median for each variable by segment, expressed as % above/below the overall average. Identify the 2–3 defining characteristics of each segment and assign a descriptive name.
5. **Validate and interpret** — confirm segments are meaningfully different (silhouette score > 0.3 for clustering) and make business sense. Sanity-check by asking whether you would actually treat each segment differently.
6. **Map to strategy and report** — assign each segment to a recommended strategy (Retain & Expand, Monetise, Activate, Win-Back, Sunset). Produce `assets/segment_profile_template.md` with the profiles and strategic priorities.

**Inputs the skill needs**
- User-level data with attributes (demographics, plan type) and behavioural metrics (sessions, revenue, feature usage, recency)
- Business goal the segmentation will serve
- Any existing segmentation to validate or replace
- Minimum of ~100 users per expected segment for clustering to be meaningful

**Output**
- `scripts/segmentation_runner.py` — runs k-means clustering, produces elbow and silhouette plots, assigns segment labels
- `references/segmentation_approaches.md` — when to use k-means vs. RFM vs. rule-based; interpretation guide
- `assets/segment_profile_template.md` — filled segment profiles with size, key characteristics, recommended strategy, and tracking plan

---

### 13. funnel-analysis

**Conversion funnel analysis with drop-off investigation. Use when analyzing multi-step processes, identifying conversion bottlenecks, comparing segments through a funnel, or optimizing user journeys.**

**When to use**
- Conversion is low and the team needs to know where users are dropping off
- A product change may have affected a specific funnel step
- Comparing conversion rates across channels, devices, or user cohorts
- Designing an A/B test and needing a baseline to set a meaningful MDE
- Building a regular funnel monitoring report

**Process**
1. **Define funnel steps and time window** — list the ordered sequence of events or pages that constitute the funnel. Agree on how long a user has to complete the funnel (session, 24 hours, 7 days). Ambiguous definitions here will invalidate the analysis.
2. **Build the user-level funnel dataset** — for each user who reached step 1, record which subsequent steps they completed and when, within the time window. Use `scripts/funnel_analyzer.py` to compute this from an events log.
3. **Calculate conversion rates** — compute step-to-step conversion (users reaching step N ÷ users reaching step N−1) and overall conversion (step 1 to last step). Record absolute drop-off counts at each step.
4. **Analyse time-to-convert** — for users who completed each step, calculate median, P75, and P95 time between steps. Long gaps can signal friction even without high drop-off.
5. **Segment the funnel** — run the funnel separately by channel, device type, user cohort, or other dimensions. Rank segments by overall conversion rate and identify where the worst-performing segment diverges from the best. See `references/funnel_design_guide.md`.
6. **Prioritise and report** — rank drop-off points by absolute users lost × estimated revenue impact. Produce `assets/funnel_report_template.md` with the funnel table, segment comparison, and ranked recommendations.

**Inputs the skill needs**
- Event log data with at minimum: user_id, event_name, timestamp
- Ordered list of funnel steps (event names in sequence)
- Time window for funnel completion
- Segmentation columns if a comparative analysis is needed (channel, device, plan)
- Estimated revenue value of a conversion (for impact sizing)

**Output**
- `scripts/funnel_analyzer.py` — builds user-level funnel from an event log, computes step conversions, drop-offs, and time-to-convert
- `references/funnel_design_guide.md` — how to define funnels, choose time windows, and avoid common measurement mistakes
- `assets/funnel_report_template.md` — report template: funnel overview table, drop-off analysis, segment comparison, time-to-convert, recommendations

---

### 14. time-series-analysis

**Temporal pattern detection and forecasting. Use when analyzing trends over time, detecting seasonality, identifying anomalies in time series, or building simple forecasting models for planning.**

**When to use**
- Building a forecast for operational planning (staffing, inventory, infrastructure capacity)
- Identifying whether a trend is genuine or driven by seasonality
- Detecting anomalies in a metric stream (traffic spikes, revenue dips, error rate surges)
- Providing a "what would have happened" baseline for measuring initiative impact
- Presenting year-over-year growth in a way that accounts for seasonal patterns

**Process**
1. **Load and inspect the time series** — confirm regular intervals (fill gaps if needed), check for obvious data quality issues (negative values, zeros in non-zero series), and identify the natural granularity (daily, weekly, monthly).
2. **Test for stationarity** — run an ADF test. If non-stationary (trend or seasonality present), note this — it informs decomposition and model choice rather than blocking analysis. See `references/ts_patterns_guide.md`.
3. **Decompose into components** — separate the time series into trend, seasonal, and residual using additive or multiplicative decomposition. Measure the strength of each component (0–1). Strong seasonality (>0.6) means raw values are misleading without seasonal adjustment.
4. **Detect anomalies** — flag points more than 3 standard deviations from the rolling median. Investigate the top 5 anomalies against the event log (product releases, campaigns, incidents). Use `scripts/ts_analyzer.py --detect-anomalies`.
5. **Fit a forecast model** — fit an ARIMA model (or simpler moving average if data is short). Validate on a held-out 20% test set and report MAPE. Generate point estimates and 95% confidence intervals for the forecast horizon.
6. **Produce the analysis report** — summarise trend direction and strength, seasonal patterns and their business implications, anomaly findings, and the forecast with uncertainty. Use `assets/ts_report_template.md`.

**Inputs the skill needs**
- Time series data: date column + one numeric metric column, minimum 2 full seasonal cycles
- Granularity of the data (daily, weekly, monthly)
- Forecast horizon required (days, weeks, months ahead)
- Event log or change log for anomaly investigation
- Business context: what drives this metric, known seasonal patterns

**Output**
- `scripts/ts_analyzer.py` — decomposes, detects anomalies, and fits an ARIMA forecast; outputs charts and CSV
- `references/ts_patterns_guide.md` — stationarity, seasonality types, model selection guide, and common pitfalls
- `assets/ts_report_template.md` — report template: characteristics, decomposition summary, anomaly list, forecast table, insights

---

### 15. root-cause-investigation

**Systematic investigation of metric changes and anomalies. Use when a metric unexpectedly changes, investigating business metric drops, explaining performance variations, or drilling into aggregated metric drivers.**

**When to use**
- A key metric dropped (or spiked) unexpectedly and the team needs an explanation
- Stakeholders are asking "why did X happen?" and need an evidence-based answer
- A metric change has been observed but the team is unsure whether it's noise or signal
- Preparing a post-mortem after an incident that affected business metrics
- A trend change happened weeks ago and needs retrospective investigation

**Process**
1. **Validate the change** — confirm the metric changed beyond normal variance using a z-score or simple comparison to the rolling average. If the change is within ±1.5 standard deviations, document it as within normal range and close. Use `scripts/drilldown_analyzer.py --validate`.
2. **Establish a timeline** — plot the metric over time to pinpoint when the change started. A sudden step change suggests a specific event; a gradual drift suggests a structural shift.
3. **Decompose the metric** — break the metric into its constituent parts (e.g., revenue = volume × price × mix). Determine which component is driving the change before drilling into dimensions.
4. **Drill down systematically** — compare the metric before vs. after the change across available dimensions (geography, platform, channel, product category, user segment). Sort by absolute contribution to identify the primary driver. Use `scripts/drilldown_analyzer.py --drilldown`. See `references/rca_framework.md` for the structured approach.
5. **Test hypotheses** — generate explicit hypotheses (volume drop, mix shift, per-unit quality change, data issue) and accept or reject each with evidence. Correlate the timeline with known events from `references/hypothesis_testing_guide.md`.
6. **Write the root cause report** — document the primary driver (quantified share of impact), supporting evidence, rejected hypotheses, and tiered recommendations (immediate / short-term / long-term). Use `assets/rca_report_template.md`.

**Inputs the skill needs**
- Metric name and historical values (at least 30 days before the change)
- Granular data with dimensional breakdowns (geography, platform, segment, etc.)
- The date or date range when the change was noticed
- A change log or incident log for the same period (product releases, campaigns, outages)
- The business context: what decisions depend on this metric

**Output**
- `scripts/drilldown_analyzer.py` — validates the change, computes dimensional drill-downs, and ranks contributors by impact
- `references/rca_framework.md` — structured five-step RCA method with decision rules
- `references/hypothesis_testing_guide.md` — checklist of common root causes and how to test each
- `assets/rca_report_template.md` — report template: what changed, when, primary driver, supporting evidence, timeline, recommendations

---

### 16. ab-test-analysis

**Rigorous A/B test statistical analysis. Use when analyzing experiment results, calculating statistical significance, checking for sample ratio mismatch, or validating test design before launch.**

**When to use**
- An experiment has finished and the team needs a ship / no-ship recommendation
- Results look directionally positive but the team is unsure if they're statistically significant
- A test has been running for weeks without a clear winner and someone needs to decide whether to continue
- A new experiment needs sample-size planning before launch
- Results are disputed and need a rigorous, documented analysis

**Process**
1. **Confirm test design** — verify the hypothesis, the control and treatment definitions, the randomisation unit (user/session/device), the primary metric, any guardrail metrics, and the target split ratio.
2. **Check for sample ratio mismatch (SRM)** — run a chi-square test on the actual vs. expected split. If SRM is detected, stop and investigate the randomisation pipeline before interpreting results. Use `scripts/ab_test_analyzer.py --check-srm`.
3. **Calculate per-variant metrics** — compute the rate (or mean) and 95% confidence interval for the primary metric in each variant. Document absolute and relative difference.
4. **Run the significance test** — execute a two-proportion z-test (for rates) or Welch's t-test (for means). Record z-score, p-value, and 95% CI for the effect. Use `references/statistical_tests_reference.md` if unsure which test applies.
5. **Check guardrail metrics** — run the same significance test for each guardrail metric. A significant degradation on any guardrail is a blocker regardless of primary metric results.
6. **Produce the recommendation** — synthesise SRM result, power, significance, and guardrail checks into a clear ship / no-ship / extend decision. Quantify the expected business impact if shipped. Record in `assets/ab_test_report_template.md`.

**Inputs the skill needs**
- Test plan or hypothesis document (variant definitions, randomisation unit, primary metric)
- Data with at minimum: user_id, variant assignment, primary metric outcome
- Optional: guardrail metric values per user, daily aggregate data for temporal validity checks
- Target split ratio (e.g., 50/50)
- Minimum detectable effect or business threshold for "worth shipping"

**Output**
- `scripts/ab_test_analyzer.py` — runs SRM check, significance test, power analysis, and guardrail checks from a CSV or summary stats input
- `references/statistical_tests_reference.md` — which test to use and when
- `references/ab_test_design_guide.md` — SRM causes, power planning, peeking and multiple testing
- `assets/ab_test_report_template.md` — structured report: design, results, checks, recommendation, expected impact

---

### 17. business-metrics-calculator

**Standard business metric calculation with industry benchmarks. Use when calculating SaaS metrics (MRR, churn, LTV, CAC), e-commerce KPIs, or product analytics metrics with proper definitions.**

**When to use**
- Preparing a board or investor deck and need accurately defined metrics
- The team disagrees on how a key metric (e.g., churn) should be calculated
- Benchmarking performance against industry standards
- Building a metrics report for a new business or new metric set
- Validating that existing metric calculations match the standard definition

**Process**
1. **Identify the business model and period** — confirm the model type (SaaS subscription, e-commerce, marketplace, product/app) and the calculation period (month, quarter, trailing 12M). Model type determines which metrics apply. See `references/metric_definitions.md`.
2. **Load and validate the underlying data** — check for expected row counts, missing values, and plausible date ranges. A metrics report is only as good as the data feeding it.
3. **Calculate primary metrics** — for SaaS: MRR, ARR, new MRR, churned MRR, expansion MRR, customer churn rate, revenue churn rate. For e-commerce: GMV, AOV, conversion rate, ROAS. Use `scripts/saas_metrics.py` or adapt for other models.
4. **Calculate unit economics** — LTV (simple average and cohort-based), CAC, LTV:CAC ratio, payback period, and quick ratio. Document which assumptions were used for LTV lifetime.
5. **Compare to benchmarks** — grade each metric against the industry benchmark thresholds in `references/metric_definitions.md` (good / average / poor). Flag anything outside the acceptable range.
6. **Produce the metrics report** — assemble results into `assets/metrics_report_template.md` with trend charts, benchmark comparison, and 3–5 key insights. Document any definition choices that differ from industry standard.

**Inputs the skill needs**
- Subscription or transaction data with at minimum: customer ID, date, value, status
- Marketing spend data (for CAC calculation)
- Monthly targets or goals (for vs-target comparisons)
- The agreed-upon metric definitions (or default to industry standard)
- Time period and any segmentation required (by plan, region, cohort)

**Output**
- `scripts/saas_metrics.py` — calculates standard SaaS metrics from a subscriptions CSV; includes MRR waterfall, churn, LTV/CAC
- `references/metric_definitions.md` — canonical definitions and benchmark thresholds by model type
- `assets/metrics_report_template.md` — structured report: revenue metrics, customer metrics, unit economics, benchmark comparison, insights

---

## Category 04 · Data Storytelling & Visualization (5 skills)

*Turn raw findings into insights that drive decisions.*

### 18. insight-synthesis

**Transform data findings into compelling insights. Use when converting analysis results into actionable insights, connecting findings to business impact, or preparing insights for stakeholder communication.**

**When to use**
- An analysis has produced many statistics but no clear "so what"
- The team has findings but is struggling to prioritise which ones to act on
- Stakeholders are asking "what does this mean for us?" rather than "what did you find?"
- Multiple analyses need to be synthesised into a unified set of recommendations
- Preparing an insight briefing for a team that doesn't have time to review the full analysis

**Process**
1. **List all findings** — enumerate every statistically meaningful finding: trends, comparisons, correlations, anomalies, surprises. Write each as a factual statement. Don't interpret yet.
2. **Apply So What → Why → Now What to each finding** — convert each fact into an insight by answering: So what (why does this matter to the business?), Why (what is the most likely explanation?), Now what (what specific action should follow?). See `references/insight_framework.md`.
3. **Quantify business impact** — for each insight, estimate the financial, customer, or operational magnitude. An insight without a number is an observation. Use order-of-magnitude estimates if precise data is not available.
4. **Prioritise by impact × confidence × actionability** — score each insight on these three dimensions (1–3 scale). Insights that score high on all three are the ones to lead with. Deprioritise insights that are high-impact but low-confidence until validated.
5. **Group and resolve conflicts** — cluster related insights and check for contradictions. If two findings point in opposite directions, document the tension and state what additional data would resolve it.
6. **Produce the insight brief** — present the top 3–5 insights in priority order, each with the finding, So What / Why / Now What, business impact, and confidence level. Use `assets/insight_brief_template.md`.

**Inputs the skill needs**
- All analysis findings (statistics, charts, model outputs, anomalies)
- Business context: current goals, OKRs, strategic priorities
- Audience who will act on the insights (role and decision authority)
- Confidence levels for the findings (based on sample size, method, data quality)
- Known constraints on action (budget, timeline, team capacity)

**Output**
- `references/insight_framework.md` — So What / Why / Now What pattern, insight quality rubric, prioritisation matrix
- `references/prioritization_guide.md` — scoring insights by impact, confidence, and actionability; how to present trade-offs
- `assets/insight_brief_template.md` — structured brief: top insights in priority order, each with impact, explanation, recommendation, and confidence level

---

### 19. visualization-builder

**Create effective, publication-ready data visualizations. Use when choosing chart types, designing presentation visuals, building dashboard charts, or applying visual design best practices to data output.**

**When to use**
- Choosing the right chart type for a specific analytical message
- A chart exists but is cluttered, misleading, or failing to make the point
- Building a chart for an executive presentation that must work without verbal explanation
- Producing consistent, branded visualisations across a report or dashboard
- Creating accessible charts that work for colorblind viewers or screen readers

**Process**
1. **Identify the message type** — classify the chart's purpose: comparison (bar), trend over time (line), composition / part-of-whole (stacked bar, pie only for 2–3 categories), distribution (histogram, box plot), or relationship (scatter). The message type determines the chart type. See `references/chart_selection_guide.md`.
2. **Select and load the data** — confirm the data is at the right grain for the chart. Aggregations (e.g., groupby month) should happen before plotting, not inside the chart library.
3. **Build the base chart** — use `scripts/chart_builder.py` with pre-set professional styling (whitegrid, sans-serif, accessible color palette). Set axes, ticks, and scale deliberately — default settings are often wrong.
4. **Apply visual hierarchy** — make the most important data element visually dominant (bolder line, darker bar, distinct color). De-emphasise secondary series. Remove every element that doesn't contribute to the message (gridlines at 0.2 alpha, no top/right spines). See `references/visual_design_principles.md`.
5. **Annotate for the reader** — add a descriptive title that states the finding ("Mobile churn is 2× desktop"), not the variable names ("Churn by device type"). Annotate key data points, thresholds, and reference lines directly on the chart. Add a data source and date.
6. **Export and validate** — export at 300 DPI for print or 150 DPI for web. View the chart at the intended display size. Check: is the key message legible in under 5 seconds? Does it work in greyscale? Complete `assets/viz_spec_template.md` if the chart is part of a larger deliverable.

**Inputs the skill needs**
- The data to be visualised (at the correct aggregation grain)
- The single key message the chart must communicate
- The audience (technical or executive) and the display context (presentation slide, report, dashboard, email)
- Brand colors or style guidelines if applicable
- Any accessibility requirements (colorblind palette, alt text)

**Output**
- `scripts/chart_builder.py` — creates professional matplotlib/seaborn charts with pre-set styling, annotation helpers, and export settings
- `references/chart_selection_guide.md` — which chart type for which message; common chart mistakes and how to fix them
- `references/visual_design_principles.md` — color, typography, hierarchy, annotation, and accessibility principles
- `assets/viz_spec_template.md` — spec template for a chart: message, data source, chart type, annotations, export requirements

---

### 20. executive-summary-generator

**Create concise executive summaries from detailed analysis. Use when preparing board decks, executive briefings, or condensing complex analysis into decision-ready formats for senior audiences.**

**When to use**
- A detailed analysis needs to be condensed to 1–2 pages for a senior audience
- An executive asks "what's the bottom line?" and a full report won't be read
- Preparing a board deck section that summarises a longer analytical workstream
- A recurring report needs to lead with the key message rather than data tables
- A decision needs to be made by end of day and the executive has 10 minutes

**Process**
1. **Extract the top 3–5 insights** — go through the full analysis and identify only the findings that change or reinforce a decision. Filter out interesting-but-not-actionable findings. If you have more than 5 insights, you haven't prioritised yet.
2. **Quantify the business impact of each insight** — every insight must carry a number: revenue at risk, cost saving, users affected, time to payback. Vague impact ("significant") does not belong in an executive summary. See `references/executive_communication.md`.
3. **Write a one-paragraph situation statement** — explain why this analysis was done, what the question was, and why the timing matters. One paragraph, no jargon.
4. **Apply the pyramid principle** — lead each insight with the conclusion ("Mobile churn is causing $800K ARR loss"), then the evidence, then the supporting detail. Never bury the finding at the end of a paragraph.
5. **State recommendations as specific actions** — each recommendation must name what to do, who is responsible, what the expected outcome is, and by when. "Improve the app" is not a recommendation.
6. **Write the decision block** — the final section names the explicit decision or approval the executive needs to give, the investment or resource required, the expected return, and the deadline. Use `assets/executive_summary_template.md` to assemble the document.

**Inputs the skill needs**
- The full analysis or report to be summarised
- Knowledge of the executive audience (role, priorities, decisions they're responsible for)
- Quantified business impact for each major finding
- Recommended actions already identified
- Format constraints (one page, two pages, specific slide count)

**Output**
- `references/pyramid_principle_guide.md` — answer-first structure, BLUF writing, how to edit a bottom-up draft into top-down
- `references/executive_communication.md` — adapting tone, removing jargon, quantifying everything, avoiding hedge language
- `assets/executive_summary_template.md` — 1–2 page template: situation, key insights (with impact), recommendations (with outcomes), decision needed

---

### 21. dashboard-specification

**Design specifications for effective dashboards. Use when planning new dashboards, improving existing ones, or documenting dashboard requirements before development starts.**

**When to use**
- A new dashboard is being built and developers need a clear brief before starting
- An existing dashboard is confusing or underused and needs a structured redesign
- Stakeholders and the data team have different ideas about what a dashboard should show
- Documenting dashboard requirements as part of a broader data product process
- Creating a self-service analytics specification that can be handed off without multiple Q&A rounds

**Process**
1. **Define the purpose** — write one sentence: "This dashboard answers [question] for [audience] who need to [decision or action]." If it can't be stated in one sentence, the scope needs narrowing first. See `references/dashboard_design_principles.md`.
2. **Profile target users** — for each audience (executive, manager, IC), document their visit frequency, the primary question they come to answer, and their technical comfort level. Users with different needs usually need different dashboards, not more filters on one.
3. **Define the metric hierarchy** — list primary KPIs (hero numbers at the top), secondary supporting metrics, and detail-level breakdowns. A dashboard with more than 10–12 distinct metrics is trying to do too much.
4. **Design the information architecture** — sketch the layout using the hero → trends → breakdowns → details pattern. Position the most important information in the top-left. Use `references/dashboard_requirements_guide.md` for layout patterns.
5. **Specify interactivity** — list global filters (date range, region, segment), drill-down paths, click actions, and hover tooltip content. Every filter and drill-down adds complexity; justify each one.
6. **Document data requirements and success criteria** — for each metric, record the source table, transformation logic, and refresh frequency. Define how dashboard success will be measured (adoption rate, reduction in ad-hoc requests). Complete `assets/dashboard_spec_template.md`.

**Inputs the skill needs**
- The business question the dashboard is meant to answer
- A list of candidate metrics (team can provide a rough list; you'll curate it)
- The primary audience (role, visit frequency, decision they make)
- Data availability: confirmed source tables and refresh schedules
- Any constraints: tool (Tableau, Looker, Metabase, etc.), branding guidelines

**Output**
- `references/dashboard_design_principles.md` — layout hierarchy, chart selection, information density guidelines
- `references/dashboard_requirements_guide.md` — how to run requirements gathering, avoid scope creep, and validate the spec
- `assets/dashboard_spec_template.md` — complete spec: purpose, users, metric hierarchy, layout wireframe, interactivity, data sources, success criteria

---

### 22. data-narrative-builder

**Build compelling data-driven narratives. Use when presenting analysis results, creating stakeholder reports, or transforming a set of findings into a story that drives a specific decision or action.**

**When to use**
- A presentation exists but feels like a data dump rather than a story
- The analysis has a clear finding but the team doesn't know how to make it compelling
- The audience is senior and will not read more than 5 slides
- A decision needs to be made and the data needs to make a clear, emotion-aware argument
- A recurring report needs to be restructured around a narrative rather than a metric list

**Process**
1. **Identify the central message** — write the single most important thing the audience should know and do after seeing this. Everything else is supporting material. If there's more than one message, there are multiple presentations.
2. **Choose a narrative framework** — select the structure that fits the context. Situation–Complication–Resolution works for most problem/solution stories. Before–After–Bridge is strong for demonstrating impact. See `references/narrative_frameworks.md` for all patterns with examples.
3. **Assign an emotional arc** — map each section to an intended emotional state: establish comfort (Situation), introduce tension (Complication), offer confidence (Resolution). Tone and data emphasis should match the intended emotion at each stage.
4. **Draft each section with data woven in** — apply the pyramid principle: lead with the conclusion, then support it with evidence. Numbers must serve the narrative, not interrupt it. Round large numbers for recall; humanise by expressing impact in terms the audience cares about.
5. **Plan the visual sequence** — assign one key chart or visual to each narrative beat. The visual should reinforce the spoken or written message, not repeat it. See `references/data_writing_guide.md` for annotation and emphasis techniques.
6. **Write the opening hook and closing call to action** — the hook must earn attention in under 10 seconds (a surprising stat, a question, or a contrast). The CTA must name a specific decision, person, and deadline. Complete `assets/narrative_template.md`.

**Inputs the skill needs**
- The central finding or insight to be communicated
- The audience (role, knowledge level, what they care about most)
- The desired action or decision at the end of the presentation
- All supporting data and charts already prepared
- Format and time constraints (slides, report, 5-minute presentation, 30-page doc)

**Output**
- `references/narrative_frameworks.md` — SCR, BAB, hero journey, and sparklines patterns with data storytelling examples
- `references/data_writing_guide.md` — pyramid principle, number formatting, annotation, plain-language techniques
- `assets/narrative_template.md` — fill-in-the-blank narrative structure: hook, situation, complication, resolution, call to action

---

## Category 05 · Stakeholder Communication (5 skills)

*Bridge the gap between technical depth and business understanding.*

### 23. technical-to-business-translator

**Translate technical analysis into business language. Use when explaining statistical concepts to non-analysts, simplifying technical findings, or bridging communication between data teams and business stakeholders.**

**When to use**
- When technical output (model results, statistical tests, query findings) needs to be understood by a business audience
- Also use to review your own writing before sending — it is easy to slip into jargon without noticing

**Process**
1. **Detect jargon** — run `scripts/jargon_detector.py` on the draft text to flag technical terms that need translation.
2. **Score readability** — run `scripts/readability_scorer.py` to get Flesch-Kincaid grade level and sentence complexity metrics; target ≤ grade 10 for executive audiences.
3. **Identify the audience persona** — use `references/stakeholder_personas.md` to select the persona that best matches your reader; each persona has vocabulary preferences and typical questions.
4. **Apply translation patterns** — use `references/translation_pattern_library.md` to swap technical language for business equivalents (e.g., "p-value < 0.05" → "we're 95% confident this isn't random chance").
5. **Replace with metaphors where needed** — for complex statistical concepts, pick an appropriate metaphor from `references/metaphor_bank.md`.
6. **Draft the translated version** — use `assets/translation_template.md` to produce the parallel technical/business version; keep the original in an appendix for technical reviewers.

**Inputs the skill needs**
- Draft technical text or findings
- Target audience role (VP, product manager, operations, finance, etc.)

**Output**
- Jargon detection report
- Readability score before/after
- Translated text with original in appendix (`translation_template.md`)

---

### 24. stakeholder-requirements-gathering

**Structured requirements elicitation for analysis requests. Use when scoping new analysis projects, clarifying ambiguous business questions, or documenting analysis acceptance criteria with stakeholders.**

**When to use**
- At the start of any non-trivial analysis request, especially when the ask is vague ("can you look into X?"), when multiple stakeholders have a stake in the outcome, or when the result will drive an important decision. Spending 30 minutes on requirements prevents days of rework.

**Process**
1. **Run the intake interview** — use the question guide in `assets/interview_guide.md` to surface: the business decision being made, who the audience is, what "done" looks like, and what constraints exist.
2. **Identify the decision type** — apply `references/decision_maker_framework.md` to classify the decision (strategic / operational / tactical) and calibrate the required rigour and format.
3. **Document requirements** — fill in `assets/requirements_doc_template.md` covering: business question, success criteria, scope inclusions/exclusions, data sources, and timeline.
4. **Resolve ambiguities** — use the elicitation techniques in `references/elicitation_techniques.md` for any requirement still unclear after the interview (5-whys, scenario walkthrough, MoSCoW prioritisation).
5. **Get explicit sign-off** — send the requirements doc to the requestor for confirmation before starting work; update based on feedback.
6. **Produce the analysis brief** — convert approved requirements into `assets/analysis_brief_template.md`, which becomes the authoritative scope document for the project.

**Inputs the skill needs**
- Stakeholder's initial request (however vague)
- Name and role of primary requestor and any other stakeholders
- Proposed deadline or urgency level

**Output**
- Completed requirements doc (`requirements_doc_template.md`)
- Analysis brief ready to hand to the analyst (`analysis_brief_template.md`)
- Interview notes (optional, for complex projects)

---

### 25. analysis-qa-checklist

**Pre-delivery quality assurance for analysis work. Use when reviewing analysis before sharing with stakeholders, checking for completeness, validating assumptions, or ensuring clarity of recommendations.**

**When to use**
- Before sharing any analysis output with a stakeholder — dashboard, report, ad-hoc query result, model output, or written findings. Run this every time, not just for big projects. The cost of a post-delivery correction is always higher than the cost of a pre-delivery check.

**Process**
1. **Run automated checks** — use `scripts/qa_runner.py` against the output file to catch numeric, structural, and formatting issues programmatically.
2. **Complete the logic checklist** — work through `references/qa_checklist_master.md` section by section: question framing, data sourcing, transformations, statistical validity, findings, and presentation.
3. **Review for common errors** — cross-check against `references/common_analysis_errors.md`; pay special attention to the top-frequency mistakes for the analysis type.
4. **Validate assumptions explicitly** — for every assumption in the analysis, verify it has a source, is documented, and the output is sensitivity-tested where the assumption is uncertain.
5. **Check the narrative** — confirm the conclusion follows from the data, caveats are stated, and the recommendation is actionable.
6. **Record sign-off** — complete `assets/qa_signoff_template.md` with reviewer, issues found, resolution status, and delivery decision.

**Inputs the skill needs**
- Output file to review (CSV, notebook, SQL result, or written doc)
- Original analysis question / brief
- Name of reviewer and intended audience

**Output**
- QA runner report (automated flags)
- Completed checklist with pass/fail per section
- Signed-off `qa_signoff_template.md` confirming delivery readiness

---

### 26. methodology-explainer

**Explain analysis methodology to diverse audiences. Use when documenting 'how we did this' sections, building trust through transparency, or teaching analytical approaches to stakeholders.**

**When to use**
- Any time you deliver findings that require the audience to trust the method — A/B tests, attribution models, forecasts, statistical analyses, or anything where "how did you get that?" is a likely question. Write the methodology section before distributing results, not after questions arrive.

**Process**
1. **Identify the audience tier** — use `references/audience_depth_guide.md` to determine the appropriate level: executive (why/what), business analyst (what/how at high level), or technical peer (full detail).
2. **Select the explanation pattern** — use `references/methodology_explanation_patterns.md` to pick the structure: narrative, layered (short summary + appendix), or Q&A format.
3. **Draft the core explanation** — cover: what question was asked, what data was used, what method was applied, what assumptions were made, and what the key limitation is.
4. **Apply plain-language rewrites** — replace statistical terms with business equivalents per the translation table in `references/methodology_explanation_patterns.md`.
5. **Add a limitations paragraph** — every methodology explanation must include at least one honest limitation and what it means for the conclusions.
6. **Produce deliverables** — write-up using `assets/methodology_writeup_template.md`; if the methodology will be presented, use `assets/methodology_slide_template.md`.

**Inputs the skill needs**
- Description of the analytical method used (technique, data, steps)
- Audience type (executive / business / technical)
- Any assumptions or known limitations

**Output**
- Plain-language methodology write-up
- Limitations section
- Completed `methodology_writeup_template.md` or `methodology_slide_template.md`

---

### 27. impact-quantification

**Estimate and communicate business impact of insights. Use when sizing opportunities discovered in analysis, calculating ROI of recommended actions, or prioritizing initiatives by potential impact.**

**When to use**
- After an analytical finding surfaces a potential action, change, or opportunity. Use to produce a defensible numeric estimate that stakeholders can act on. Also use when prioritizing a backlog of initiatives — quantified impact is the primary ranking signal.

**Process**
1. **Classify the impact type** — revenue growth, cost reduction, risk reduction, or efficiency gain. Each type has a different formula family (see `references/impact_quantification_framework.md`).
2. **Gather inputs** — collect baseline metrics, affected population size, expected lift/reduction, time horizon, and confidence level.
3. **Build the point estimate** — use `scripts/revenue_impact.py` for revenue/growth scenarios or `scripts/cost_savings.py` for cost/efficiency scenarios.
4. **Add uncertainty bounds** — use `scripts/confidence_interval.py` to produce low/base/high estimates. Never deliver a single number without a range.
5. **Document assumptions** — fill in `references/assumption_documentation.md` for every input that is estimated rather than directly measured; note the sensitivity of the output to each.
6. **Package the estimate** — complete `assets/impact_estimate_template.md` with the range, assumptions, confidence, and recommended action; optionally build the full `assets/business_case_template.md` for larger decisions.

**Inputs the skill needs**
- Baseline metric value (current state)
- Affected population or volume
- Expected change (lift %, absolute, or rate change)
- Time horizon (monthly / annual)
- Confidence level in inputs (high / medium / low)

**Output**
- Impact estimate with low/base/high range
- Assumption log (source and sensitivity for each input)
- Completed `impact_estimate_template.md` or `business_case_template.md`

---

## Category 06 · Workflow Optimization (4 skills)

*Work smarter across every project.*

### 28. analysis-planning

**Structure analysis approach before starting work. Use when receiving new analysis requests, breaking down complex questions into steps, or planning iterative analysis workflows.**

**When to use**
- After requirements are gathered and before any data is touched. Planning is especially important when the analysis involves multiple steps, uncertain data availability, or a tight deadline where sequencing matters. A 15-minute planning session prevents hours of wrong-direction work.

**Process**
1. **Decompose the question** — break the business question into sub-questions using `references/scoping_framework.md`; each sub-question should be answerable with a single data pull or calculation.
2. **Identify data dependencies** — for each sub-question, list the required tables/datasets and assess availability (confirmed / likely / unknown); flag blockers early.
3. **Sequence the work** — order sub-questions so that each output feeds the next; identify which steps can run in parallel.
4. **Estimate effort** — use `references/effort_estimation.md` to assign time estimates per step; sum to a total and compare against the deadline.
5. **Log risks and dependencies** — use `references/risks_dependencies.md` to document anything that could delay or invalidate the plan (data gaps, external approvals, methodology uncertainty).
6. **Produce the plan** — fill in `assets/analysis_plan_template.md`; for projects with stakeholder kickoffs use `assets/kickoff_doc_template.md`.

**Inputs the skill needs**
- Analysis brief or requirements doc (from `stakeholder-requirements-gathering` skill)
- Available data sources
- Deadline and resource constraints

**Output**
- Completed analysis plan with sequenced steps and time estimates (`analysis_plan_template.md`)
- Kickoff doc for stakeholder alignment (optional, `kickoff_doc_template.md`)
- Risk / dependency log

---

### 29. context-packager

**Efficiently package context for AI-assisted analysis. Use when preparing to work with Claude on analysis, organizing context documents, or structuring prompts for complex analytical tasks.**

**When to use**
- Before starting an AI-assisted analysis session when the task requires more than a single prompt — complex investigations, multi-step analyses, or work that depends on project-specific knowledge. A well-packaged context bundle reduces back-and-forth and produces better first responses.

**Process**
1. **Identify required context layers** — use `references/context_layering_guide.md` to decide which layers are needed: task definition, business context, data schema, prior findings, constraints, and output format.
2. **Collect and deduplicate sources** — run `scripts/context_bundler.py` to merge multiple context files into a single structured bundle; it deduplicates and applies the layering order.
3. **Check token budget** — run `scripts/token_counter.py` on the bundle to estimate token count; trim lower-priority layers if over budget (see `references/context_layering_guide.md` for trimming priority).
4. **Score context quality** — evaluate the bundle against `references/context_quality_rubric.md`; a good bundle scores ≥ 7/10 on completeness, clarity, and relevance.
5. **Write the prompt header** — prepend a clear task statement to the bundle: what you need, what output format you expect, and any hard constraints.
6. **Save the package** — store the bundle using `assets/context_package_template.md` so it can be reused or updated for follow-up sessions.

**Inputs the skill needs**
- Task description (what you want the AI to do)
- List of context source files or snippets (schema docs, prior reports, business definitions)
- Token budget (default: 100k tokens)

**Output**
- Merged context bundle (single text file)
- Token count estimate
- Context quality score
- Ready-to-use prompt with task header (`context_package_template.md`)

---

### 30. peer-review-template

**Structured peer review for analytical work. Use when reviewing teammates' analysis, providing constructive feedback, or establishing analysis quality standards.**

**When to use**
- Before any analysis that will influence a significant decision is delivered to stakeholders. Peer review should be part of the standard delivery checklist for: dashboards going into production, reports used for strategic decisions, A/B test conclusions, and any analysis that will be cited externally.

**Process**
1. **Agree scope of review** — clarify with the author what kind of review is needed: logic check, statistical validity, code review, or presentation clarity. Use `references/peer_review_framework.md` to set expectations.
2. **Review analytical rigour** — work through `references/analytical_rigor_checklist.md`: are the question and method aligned? Are assumptions valid? Is the conclusion supported by the data?
3. **Review code or SQL** — if the analysis involves code, apply `references/code_review_for_analysis.md`: reproducibility, correctness, readability, and performance.
4. **Write feedback** — use the feedback structure in `assets/peer_review_template.md`: must-fix issues, should-fix suggestions, and optional improvements. Be specific; "this is unclear" is not actionable.
5. **Author responds** — the author addresses each point and notes disposition (fixed / accepted as-is with rationale / deferred); use `assets/review_response_template.md`.
6. **Close the review** — reviewer confirms must-fix items are resolved and signs off; document the outcome in `assets/peer_review_template.md`.

**Inputs the skill needs**
- Analysis output to review (notebook, report, dashboard spec, or SQL)
- Review scope agreed with author
- Reviewer name and role

**Output**
- Completed review with categorised feedback (`peer_review_template.md`)
- Author response log (`review_response_template.md`)
- Sign-off confirmation

---

### 31. analysis-retrospective

**Post-analysis learning and process improvement. Use when completing major analysis projects, documenting lessons learned, or improving team analytical practices.**

**When to use**
- Within one week of completing a significant analysis project — while the details are still fresh. Also use after an analysis that went wrong (late delivery, stakeholder rejection, data error discovered post-delivery) to prevent recurrence. Run team retros quarterly even without a specific incident.

**Process**
1. **Time-box the retro** — 30 minutes for solo, 60 minutes for team. Use the structured format in `references/retro_frameworks.md` to stay focused (Start/Stop/Continue or 4Ls: Liked/Lacked/Learned/Longed for).
2. **Review the project against plan** — compare actual timeline, scope, and effort to what was planned; note the gaps.
3. **Identify what went well** — capture at least two things that worked and should be repeated; these are as important as problems.
4. **Identify root causes of issues** — for each problem, apply 5-whys to find the actual cause rather than the symptom.
5. **Capture reusable learning** — use `references/learning_capture.md` to decide which learnings belong in: templates, reference docs, checklists, or team norms.
6. **Record and track actions** — fill in `assets/retrospective_template.md` with owners and due dates; log durable learnings in `assets/learnings_log_template.md`.

**Inputs the skill needs**
- Completed analysis project (name, scope, timeline)
- Original plan or brief (for comparison)
- Participants (solo or team members involved)

**Output**
- Completed retrospective (`retrospective_template.md`) with what-went-well, issues, root causes, and action items
- Learnings log entry (`learnings_log_template.md`) for reusable insights

---

## Common Skill Chains

- **New dataset**: `programmatic-eda` → `data-quality-audit` → analysis skills
- **Metric definition**: `semantic-model-builder` → `analysis-documentation`
- **Delivering findings**: `insight-synthesis` → `technical-to-business-translator` → `executive-summary-generator`
- **Any analysis**: `analysis-qa-checklist` + `analysis-assumptions-log` as quality gates
- **Weekly metrics review**: programmatic-eda → business-metrics-calculator → time-series-analysis → root-cause-investigation (if issues) → executive-summary-generator
- **New dataset investigation**: programmatic-eda → schema-mapper → semantic-model-builder → analysis skills
- **Ad-Hoc analysis request**: stakeholder-requirements-gathering → analysis-planning → relevant analysis skills → methodology-explainer → analysis-qa-checklist

## Learning Path

- **Week 1 — Foundation**: Use `programmatic-eda` on 3 different datasets; notice what context gets requested; try different levels of context
- **Week 2–3 — Core toolkit**: Set up `semantic-model-builder` for key metrics; add `query-validation` to SQL workflow; pick 2 analysis skills (cohort/funnel/segmentation)
- **Week 4+ — Advanced**: Chain 4–5 skills end-to-end on a full project; add company-specific references; build team context documents

## Examples

**Example 1 — Exploratory Data Analysis**
```
You: "I need to do exploratory data analysis on my customer dataset"
Agent: Requests dataset, business context (what one row represents), and quality thresholds
You: [provides CSV file and context]
Agent: Runs systematic EDA with quality checks, produces profiling report and findings summary
```

**Example 2 — SQL Query Review**
```
You: "Can you review this SQL query for performance issues?"
Agent: Requests query, database type, schema
You: [provides query and context]
Agent: Validates logic, checks performance, suggests optimizations
```

**Example 3 — Cohort Retention**
```
You: "I want to analyze user retention by signup month"
Agent: Requests dataset, cohort definition, retention metric
You: [provides user activity data]
Agent: Builds retention matrices, creates visualizations, interprets findings
```

**Example 4 — Metric Documentation**
```
You: "Help me document our MRR calculation"
Agent: Requests calculation logic, business context
You: [explains how MRR is calculated]
Agent: Creates structured YAML documentation optimized for dbt Semantic Layer use
```

