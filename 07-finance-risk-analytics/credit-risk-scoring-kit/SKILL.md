---
name: credit-risk-scoring-kit
description: Build credit-style risk scores — target definition, reject inference awareness, scorecard/ML modeling, calibration to PD, cut-off strategy with portfolio math. Activate for lending, B2B payment terms, or any "who will pay us back" problem.
---

# When to use
- Onboarding decisions need consistent risk assessment
- Manual credit review can't scale
- Existing score performance needs refresh or explanation

# Process
1. **Define the event** — default/delinquency precisely (90+ DPD within 12 months?), observation and outcome windows; document why these windows match the business cycle.
2. **Population honesty** — model only on approved applicants; flag reject-inference bias explicitly; monitor population stability (PSI) between development and current books.
3. **Feature discipline** — bureau attributes, behavioral history, stability signals; check availability at decision time; WOE/binning for scorecard interpretability or GBM with monotonic constraints.
4. **Calibration** — output must be a usable probability of default (Platt/isotonic), not just a ranking; validate on out-of-time sample.
5. **Cut-off economics** — plot approval rate vs expected loss vs profit per applicant; choose operating point from the trade-off curve with finance, not by AUC.
6. **Governance artifacts** — reason codes/adverse-action mapping for declines, champion/challenger process, annual validation schedule.

# Inputs the skill needs
- Required: application + performance history data
- Optional: external bureau attributes, regulatory constraints

# Output
- Calibrated risk score with documented methodology
- Cut-off recommendation with approval-rate/loss/profit curves
- Reason-code mapping and monitoring plan

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/credit_scorer.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/credit_scoring_reference.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/model_package_template.md` - Fill this template - it IS the deliverable format.
