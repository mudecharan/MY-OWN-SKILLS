---
name: outlier-triage
description: Detect, classify, and decide on outliers — separating data errors from genuine extreme values, with documented treatment per case. Activate before averages, regressions, forecasts, or anything sensitive to extreme values.
---

# When to use
- A few giant transactions distort every average you compute
- Model residuals show suspicious leverage points
- Anomaly detection itself is the goal (fraud, incidents)

# Process
1. **Multi-method detection** — run IQR fences, z-score (|z|>3), MAD-based modified z, and isolation-forest-style multivariate checks; note which points ALL methods agree on.
2. **Contextualize** — an outlier globally may be normal within its segment; re-check within meaningful groups (region × product × month).
3. **Classify each flagged point**: (a) data error → trace to source, correct if provable; (b) legitimate extreme → keep, use robust statistics; (c) out-of-scope population → exclude with documented rule.
4. **Sensitivity testing** — recompute headline metrics with and without outliers; report both when the delta is material (>5% shift).
5. **Treatment implementation** — winsorize/cap/log-transform/robust estimators as appropriate; never silently delete.
6. **Audit trail** — log every excluded point with ID, value, reason, and who approved.

# Inputs the skill needs
- Required: dataset and variables of interest
- Optional: business plausibility bounds ("orders can't exceed $50k"), known events (Black Friday spikes are real)

# Output
- Outlier register: point, method(s) that flagged it, classification, action taken
- Sensitivity table: metrics with/without outliers
- Reusable cleaning function with parameters documented

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/outlier_detector.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/outlier_scan.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/value_range_validator.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/business_rule_patterns.md` - apply these proven patterns
- `references/treatment_playbook.md` - follow these rules when classifying/deciding

### assets/ - templates to fill and deliver
- `assets/outlier_register_template.md` - Fill this template - it IS the deliverable format.
