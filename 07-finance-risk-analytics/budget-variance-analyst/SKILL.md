---
name: budget-variance-analyst
description: Analyze actual-vs-budget/variance performance — decomposition of drivers, favorable/unfavorable classification, volume-mix-price effects, forward-looking re-forecast. Activate for monthly/quarterly financial reviews.
---

# When to use
- Monthly close reviews and variance commentary writing
- Explaining to leadership why numbers beat or missed plan
- Rolling forecasts and mid-year re-plans

# Process
1. **Data assembly** — align actuals vs budget on identical dimensions (account, cost center, period); reconcile category mappings first — most "variance" is mapping noise.
2. **Variance triage** — rank all variances by absolute impact; investigate only material items (e.g., >5% AND >$10k threshold); classify timing (will reverse) vs permanent.
3. **Driver decomposition** — split revenue variance into volume × price × mix; cost variance into rate × usage; show the math, not just the total.
4. **Commentary discipline** — each material variance gets: what, why (root cause), so-what (impact if persists), action; ban "timing" as an unexplained catch-all.
5. **Re-forecast** — project full-year using run-rates adjusted for known one-offs; compare against original budget to expose planning bias patterns over time.
6. **Feedback loop** — track which cost centers systematically miss plan; that's a forecasting-process finding, not a performance finding.

# Inputs the skill needs
- Required: actuals, budget/plan, chart of accounts mapping
- Optional: prior-year actuals, driver data (units, headcount, prices)

# Output
- Variance report with ranked, decomposed explanations
- Full-year re-forecast with assumptions listed
- Commentary text ready for the finance review deck

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/drilldown_analyzer.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/variance_decompose.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/variance_methods.md` - read before starting.

### assets/ - templates to fill and deliver
- `assets/rca_report_template.md` - Fill this template - it IS the deliverable format.
- `assets/variance_report_template.md` - Fill this template - it IS the deliverable format.
