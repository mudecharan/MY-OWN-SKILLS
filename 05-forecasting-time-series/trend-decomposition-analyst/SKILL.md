---
name: trend-decomposition-analyst
description: Separate genuine trend from noise, cycles, and one-offs in business metrics — with change-point detection and honest extrapolation limits. Activate when a metric "is going up" and decisions hang on whether that's real.
---

# When to use
- Leadership asks "is growth real or just a spike?"
- Setting targets based on historical trajectory
- Detecting when a metric's behavior structurally changed (new pricing, market shift)

# Process
1. **Noise floor first** — quantify metric volatility (CV, week-over-week std); a "trend" smaller than the noise floor over a short window is not evidence.
2. **Decompose** — STL or model-based decomposition; report trend component separately from seasonal and remainder.
3. **Change-point detection** — CUSUM/PELT/Bayesian online changepoint to find structural breaks; annotate each with candidate business causes (launch, price change, market event).
4. **Segment the trend** — compute growth rates per stable segment (pre/post changepoint); a single "average growth rate" across a break is misleading.
5. **Honest extrapolation** — project trend forward ONLY with stated assumptions and widening uncertainty; never linear-extrapolate beyond 1–2 periods without justification; scenario bands (base/bull/bear) beat point estimates.
6. **Counter-check** — does the trend survive per-segment analysis, or is it one segment dragging the aggregate (Simpson's paradox check)?

# Inputs the skill needs
- Required: metric time series, known business events timeline
- Optional: segment dimensions for paradox checks

# Output
- Trend narrative: real vs noise verdict with evidence
- Change-point table with business-cause hypotheses
- Scenario projection bands with explicit assumptions

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/trend_analysis.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/ts_analyzer.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/trend_rules.md` - apply these rules; they override defaults

### assets/ - templates to fill and deliver
- `assets/trend_verdict_template.md` - Fill this template - it IS the deliverable format.
- `assets/ts_report_template.md` - Fill this template - it IS the deliverable format.
