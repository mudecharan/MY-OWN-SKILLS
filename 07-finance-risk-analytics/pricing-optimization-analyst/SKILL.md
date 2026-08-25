---
name: pricing-optimization-analyst
description: Analyze price sensitivity and recommend pricing changes — elasticity estimation, segment differentiation, promotion effectiveness, margin-volume trade-offs. Activate when prices, discounts, or packaging are on the table.
---

# When to use
- Margin pressure demands price action but elasticity is unknown
- Discounting is rampant and undisciplined
- Introducing tiered/packaged pricing

# Process
1. **Transaction forensics** — reconstruct realized price (after all discounts) by segment/product/time; quantify discount leakage — who gets them and does volume follow?
2. **Elasticity estimation** — exploit natural variation (price tests, regional differences, cost pass-through events) rather than naive price-vs-quantity correlation; log-log regression with fixed effects where panel data allows; state identification caveats honestly.
3. **Segment differentiation** — willingness-to-pay proxies by segment (order size, industry, usage intensity); find segments with statistically distinct elasticities.
4. **Promotion audit** — incremental lift vs baseline (pre/post with control group); compute promo ROI including pull-forward and pantry-loading effects.
5. **Scenario engine** — simulate margin/volume outcomes of proposed price moves using estimated elasticities; show profit-maximizing direction per segment with confidence bounds.
6. **Test plan** — design a controlled price test (geo or cohort split) to validate before full rollout; define success metrics up front.

# Inputs the skill needs
- Required: transaction-level sales data with prices/discounts/costs
- Optional: competitor prices, past price-change events

# Output
- Elasticity estimates with confidence intervals and caveats
- Segment-level pricing scenario table (margin vs volume)
- Validated price-test design ready to launch

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/elasticity_scenarios.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/pricing_reference.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/pricing_analysis_template.md` - Fill this template - it IS the deliverable format.
