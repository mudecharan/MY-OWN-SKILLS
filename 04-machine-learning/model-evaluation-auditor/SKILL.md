---
name: model-evaluation-auditor
description: Rigorous, leakage-proof model evaluation — proper splitting strategy, metric selection by problem shape, calibration checks, slice-based fairness review. Activate before trusting ANY reported model score.
---

# When to use
- A model shows great offline metrics but disappoints live
- Comparing candidate models for a decision
- Reviewing someone else's model work

# Process
1. **Split integrity audit** — time-based splits for temporal data (never random!); group-aware splits when entities repeat (same customer in train AND test inflates scores); verify no leakage via feature-availability timeline.
2. **Metric selection** — ranking problems → PR-AUC / precision@k (not ROC-AUC on imbalanced data); calibrated probabilities needed → Brier score + reliability curve; regression → pinball loss if quantiles matter.
3. **Calibration check** — predicted-vs-actual by decile; if decisions use probability thresholds, recalibrate (isotonic/Platt) on validation data.
4. **Threshold economics** — sweep thresholds against the actual cost matrix; report the profit-maximizing operating point, not default 0.5.
5. **Slice review** — performance by key segments (region, device, tenure); a model that's great on average but fails a major segment will fail publicly.
6. **Bootstrap confidence** — CIs on headline metrics via bootstrap; differences between models must exceed CI overlap to declare a winner.

# Inputs the skill needs
- Required: trained model(s), held-out data, how predictions will be used
- Optional: cost matrix, segment definitions, regulatory constraints

# Output
- Evaluation report: honest metrics with CIs, calibration plot, slice table
- Leakage/split-integrity verdict
- Recommended operating threshold with expected business value

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/evaluate_audit.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/metric_selection.md` - read before starting.

### assets/ - templates to fill and deliver
- `assets/evaluation_report_template.md` - Fill this template - it IS the deliverable format.
