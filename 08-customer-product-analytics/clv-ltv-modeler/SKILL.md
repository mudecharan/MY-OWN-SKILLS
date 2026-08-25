---
name: clv-ltv-modeler
description: Model customer lifetime value — from simple historic CLV to probabilistic BTYD models (BG/NBD + Gamma-Gamma) — for acquisition budgeting and value-based segmentation. Activate when "what is a customer worth?" drives spend decisions.
---

# When to use
- CAC targets need a defensible LTV benchmark
- Marketing budget allocation across acquisition channels
- Identifying high-future-value customers early

# Process
1. **Scope the definition** — margin-based (not revenue), over what horizon, discount rate applied; state it in one formula sentence everyone signs.
2. **Historic CLV baseline** — cohort curves: cumulative margin per customer by monthly cohort; observe saturation point to pick empirical horizon.
3. **Probabilistic upgrade** — BG/NBD (or Pareto/NBD) for purchase frequency + survival, Gamma-Gamma for monetary value; requires only RFM data; validate by predicting holdout-period purchases.
4. **Forward CLV** — per-customer expected future value; validate calibration (predicted vs actual by decile on holdout).
5. **Decision integration** — LTV:CAC ratio by channel/cohort (kill channels below threshold); early-life leading indicators of high CLV for targeting; value-based segments feeding the segmentation skill.
6. **Caveats** — non-contractual businesses have no observed churn; state model assumptions where they bite.

# Inputs the skill needs
- Required: transaction history (customer, date, amount/margin)
- Optional: CAC by channel, margin data at line level

# Output
- Cohort CLV curves + calibrated forward-LTV per customer
- LTV:CAC analysis by channel with budget implications
- High-CLV-potential early-indicator list for targeting

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/clv_model.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/cohort_builder.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/cohort_query.sql` - Run against your warehouse (adapt dialect); capture results as evidence.
- `scripts/cohort_visualizer.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/retention_matrix.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/clv_reference.md` - read before executing the Process
- `references/retention_metrics_glossary.md` - consult for terminology alignment

### assets/ - templates to fill and deliver
- `assets/clv_report_template.md` - Fill this template - it IS the deliverable format.
- `assets/cohort_report_template.md` - Fill this template - it IS the deliverable format.
- `assets/retention_matrix.html` - Styled output format - generate/populate and deliver.
