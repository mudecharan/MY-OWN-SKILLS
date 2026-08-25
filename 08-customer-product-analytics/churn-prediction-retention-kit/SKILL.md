---
name: churn-prediction-retention-kit
description: Predict which customers will churn AND design the retention response — risk scoring, drivers, intervention targeting with expected-save value math. Activate when retention needs to become proactive instead of reactive.
---

# When to use
- Churn is discovered at cancellation, too late to intervene
- Retention budget must target the right customers
- Leadership asks "why do customers leave and who's next?"

# Process
1. **Define churn for THIS business** — contractual (cancellation) vs behavioral (inactivity window validated against return-rate curve); voluntary vs involuntary separated.
2. **Risk model** — survival analysis or classification on pre-churn behavior signals (usage decline velocity, support contacts, billing failures); time-based split mandatory; report lift in deciles ("top decile churns 8× average").
3. **Driver extraction** — SHAP/coefficients per segment; separate actionable drivers (usage, price plan) from fixed traits (tenure) — only actionable ones inform plays.
4. **Save-value matrix** — cross risk score × save rate × customer value; the best intervention targets are high-risk × savable × valuable; low-value/high-risk → cheap automation or let go.
5. **Intervention design** — map plays per driver (onboarding call for usage-decliners, plan switch for price-driven); each play gets an owner and a measurement A/B test.
6. **Operate** — weekly risk list refresh delivered to CS with play recommendations; track saves and model decay quarterly.

# Inputs the skill needs
- Required: customer activity history, subscription/billing data, churn outcomes
- Optional: support tickets, NPS responses, past win-back results

# Output
- Churn model with decile-lift table and driver report
- Save-value matrix identifying intervention sweet spots
- Weekly operational risk-list spec + play library

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/churn_model.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/churn_reference.md` - read before executing the Process
- `references/cohort_definition_patterns.md` - apply these proven patterns

### assets/ - templates to fill and deliver
- `assets/program_design_template.md` - Fill this template - it IS the deliverable format.
