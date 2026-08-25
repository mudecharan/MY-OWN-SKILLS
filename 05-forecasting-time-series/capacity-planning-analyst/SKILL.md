---
name: capacity-planning-analyst
description: Forecast workload and translate it into staffing/resource plans — Erlang-based support models, utilization targets, scenario planning, hiring timelines. Activate when demand must become people or infrastructure.
---

# When to use
- Support/sales/ops teams need headcount plans tied to demand
- Infrastructure sizing for expected load
- Justifying (or challenging) a hiring request with math

# Process
1. **Demand forecast** — project workload volume (tickets, calls, jobs) using the demand-forecast approach at the planning granularity (interval for support, month for hiring).
2. **Work content** — measure handling time per unit (AHT) including wrap-up; separate by complexity tier; include shrinkage (breaks, training, absence — typically 25–35%).
3. **Capacity math** — required FTE = (forecast volume × AHT) / (available minutes × (1 − shrinkage) × occupancy target); use Erlang C for interval-level support staffing to respect service levels.
4. **Utilization guardrail** — plan for 75–85% occupancy, not 100%; above that, burnout and SLA collapse compound.
5. **Scenario grid** — base/high/low demand × attrition assumptions; show when capacity breaks under each; hiring lead time must precede the break date.
6. **Efficiency levers** — quantify each option (self-service deflection, AHT reduction, schedule optimization) in FTE-equivalents so trade-offs are explicit.

# Inputs the skill needs
- Required: historical workload volumes, handling times, current staffing & shrinkage
- Optional: service-level targets, attrition rates, hiring lead times

# Output
- Staffing/resource plan by period with formulas shown
- Scenario table showing break-points
- Lever analysis quantifying alternatives to hiring

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/capacity_calc.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/capacity_formulas.md` - read before starting.

### assets/ - templates to fill and deliver
- `assets/capacity_plan_template.md` - Fill this template - it IS the deliverable format.
