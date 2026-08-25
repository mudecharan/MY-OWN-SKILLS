---
name: etl-pipeline-blueprint
description: Design and implement robust extract-transform-load pipelines — ingestion patterns, idempotency, error handling, backfills, monitoring. Activate when data must move reliably from source to analytical store on a schedule.
---

# When to use
- A recurring manual export must be automated
- Pipeline failures wake people up and need root-cause discipline
- Backfilling history after a logic change

# Process
1. **Source survey** — API/file/database? Rate limits, pagination, incremental cursors (updated_at, CDC logs), auth refresh mechanics.
2. **Contract first** — define output schema, grain, SLAs (freshness, completeness), and how upstream breaking changes will be detected (schema drift checks).
3. **Design for idempotency** — every load re-runnable without duplicates: delete+insert windows, MERGE on natural key, or append-only with dedup views.
4. **Implement with guardrails** — row-count anomaly checks vs 7-day average, not-null/not-constant assertions, quarantine table for rejected records.
5. **Failure playbook** — retry policy (exponential backoff), alert routing, and a written triage order (source down? schema changed? volume shift?).
6. **Backfill procedure** — parameterized date-range runner, throttled to respect sources, validated slice-by-slice.
7. **Operate** — runbook doc: what runs when, dependencies, ownership, recovery steps.

# Inputs the skill needs
- Required: source system details, destination warehouse/storage, orchestration tool available (Airflow, Dagster, cron, GitHub Actions)
- Optional: SLA expectations, downstream consumers

# Output
- Working pipeline code (Python/SQL orchestrated)
- Runbook + failure playbook
- Data-quality assertion results from first runs

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/incremental_loader.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/idempotency_patterns.md` - apply these proven patterns

### assets/ - templates to fill and deliver
- `assets/pipeline_runbook_template.md` - Fill this template - it IS the deliverable format.
