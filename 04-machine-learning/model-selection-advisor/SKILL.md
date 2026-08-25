---
name: model-selection-advisor
description: Choose the right algorithm deliberately — start from baselines, escalate only with evidence, balancing accuracy vs interpretability vs latency vs maintainability. Activate at the start of any modeling effort or when a complex model under-delivers.
---

# When to use
- Temptation to jump straight to deep learning / XGBoost on tabular data
- A black-box model faces pushback from risk/compliance stakeholders
- Latency or retraining constraints constrain the option space

# Process
1. **Constraint inventory** — interpretability requirements, scoring latency budget, retraining frequency, team maintenance skills, serving infrastructure.
2. **Baseline ladder** — always establish in order: (a) historical average/rules, (b) regularized linear/logistic, (c) gradient-boosted trees (tabular champion), (d) neural nets ONLY for text/image/sequence or proven uplift.
3. **Fair comparison protocol** — identical splits, identical features where fair, repeated CV; record accuracy AND training/inference time per rung.
4. **Escalate only on evidence** — move up a rung only if gain > noise (bootstrap CIs) AND worth the added complexity cost.
5. **Interpretability layer** — SHAP summary for tree models; coefficient tables with standardized features for linear; pick the simplest model whose explanation stakeholders accept.
6. **Document the decision** — one-page rationale: options considered, results, why the winner won, known trade-offs accepted.

# Inputs the skill needs
- Required: framed ML problem (target, unit), training dataset size/type
- Optional: latency/interpretability constraints, existing models to beat

# Output
- Baseline-ladder experiment results table
- Selected model with documented justification
- Interpretation artifacts (SHAP plots / coefficients) matched to audience

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/baseline_ladder.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/model_choice_rules.md` - apply these rules; they override defaults

### assets/ - templates to fill and deliver
- `assets/selection_record_template.md` - Fill this template - it IS the deliverable format.
