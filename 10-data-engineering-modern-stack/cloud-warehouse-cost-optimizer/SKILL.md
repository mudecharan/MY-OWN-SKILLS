---
name: cloud-warehouse-cost-optimizer
description: Cut cloud data-warehouse spend (Snowflake/BigQuery/Redshift/Synapse) without breaking consumers — query auditing, warehouse sizing, storage lifecycle, chargeback visibility. Activate when the data bill surprises finance.
---

# When to use
- Monthly warehouse costs growing faster than usage
- Identifying who/what burns credits
- Setting cost governance before growth makes it worse

# Process
1. **Consumption audit** — rank queries by total cost (credits × frequency), not just single-run time; identify the top 10 culprits — usually 5–10 patterns = 60%+ of spend.
2. **Quick wins** — kill SELECT * habits, stop dashboard auto-refresh storms, cache-friendly materialization for repeated identical queries, right-size virtual warehouses (most are 2–4× oversized).
3. **Workload routing** — separate warehouses per workload class (ELT vs BI vs ad-hoc) with auto-suspend ≤60s; scale-out instead of scale-up for concurrency.
4. **Storage lifecycle** — Time Travel/Fail-safe retention tuning, archive cold partitions to object storage, drop zombie tables and orphan clones.
5. **Developer guardrails** — cost-per-query estimates surfaced pre-execution in dev, result-set limits on exploratory tools, query tags for attribution.
6. **Chargeback & culture** — per-team cost dashboards; monthly review; celebrate the biggest reduction, not just flag the biggest spender.

# Inputs the skill needs
- Required: access to account usage/query-history views
- Optional: budget targets, team attribution mapping

# Output
- Cost-culprit report with ranked savings opportunities
- Implemented optimizations with before/after spend evidence
- Governance policy: tagging, sizing standards, review cadence

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/cost_audit_queries.sql` - Run against your warehouse (adapt dialect); capture results as evidence.

### references/ - knowledge to read
- `references/cost_reference.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/cost_audit_template.md` - Fill this template - it IS the deliverable format.
