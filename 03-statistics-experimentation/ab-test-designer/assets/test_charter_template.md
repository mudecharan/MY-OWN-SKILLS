# A/B Test Charter — <experiment name>

## 1. Hypothesis (one sentence)
"Changing <X> will move <primary metric> from <baseline> to <target> because <mechanism>."

## 2. Design
| Item | Value |
|---|---|
| Primary metric (ONE) | |
| Secondary metrics (≤5) | |
| Guardrail metrics (≥2) + abort thresholds | |
| Randomization unit | user (hash salted) |
| Baseline / MDE / alpha / power | |
| Required n per arm / expected runtime | |
| Stopping rule | fixed-horizon OR group-sequential (declared pre-launch) |

## 3. Launch checks
- [ ] SRM check coded (arms within 0.5% of intended split)
- [ ] Contamination audit: no cross-arm leakage (shared carts, redirects)
- [ ] Event instrumentation verified end-to-end with test orders
- [ ] Guardrail dashboards live before traffic ramps

## 4. Run discipline
- [ ] No metric peeking for ship decisions before planned horizon
- [ ] Novelty check: compare week-1 vs week-2 treatment effect

## 5. Decision memo (fill at conclusion)
| Field | Value |
|---|---|
| Result (effect + CI in business units) | |
| Guardrails status | |
| Segments with divergent effects | |
| Decision: ship / iterate / kill | |
| Expected annualized impact | |
