---
name: kpi-framework-designer
description: Design a coherent KPI system — metric trees linking strategy to daily metrics, definitions with owners, targets, anti-gaming rules. Activate when the org drowns in numbers but lacks direction.
---

# When to use
- Dashboards full of metrics but no shared definition of success
- Teams optimize locally while global performance stagnates
- New leadership needs a measurement reset

# Process
1. **Strategy decomposition** — from the top goal, build a metric tree: outcome KPI → driver KPIs → diagnostic/leverage metrics; every branch answers "what causes movement in the parent?"
2. **Definition rigor** — for each KPI: exact formula, grain, source table, refresh cadence, owner (a person, not a team), and exclusions; ambiguity here is where dashboard disputes breed.
3. **Target setting** — baselines from history, targets from strategy math (e.g., "to hit $50M ARR at current churn, need X new logos/month"); stretch vs committed clearly labeled.
4. **Balance & anti-gaming** — pair every efficiency metric with a quality counterweight (speed + CSAT, volume + accuracy); run a pre-mortem: "how would a team hit this number while hurting the business?" and add guards.
5. **Cadence design** — who reviews what, when, at which meeting; kill metrics nobody acts on for two cycles.
6. **Rollout** — one-page scorecard per team, linked tree view, definition catalog as the single source of truth.

# Inputs the skill needs
- Required: strategic goals, existing metric usage inventory
- Optional: industry benchmarks for target sanity checks

# Output
- Metric tree diagram (strategy → drivers → diagnostics)
- KPI definition catalog (formula, owner, source, target)
- Review-cadence plan and anti-gaming guardrails

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/kpi_validator.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/saas_metrics.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/kpi_design_rules.md` - apply these rules; they override defaults
- `references/metric_definitions.md` - read before starting.

### assets/ - templates to fill and deliver
- `assets/kpi_framework_template.md` - Fill this template - it IS the deliverable format.
- `assets/metrics_report_template.md` - Fill this template - it IS the deliverable format.
