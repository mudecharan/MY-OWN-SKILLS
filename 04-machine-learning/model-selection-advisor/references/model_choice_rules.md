# Model Choice Rules

## The ladder (never skip rungs)
1. **Rules / historical average** — sometimes beats ML; establishes floor.
2. **Regularized linear / logistic** — strong on tabular, interpretable, fast.
3. **Gradient-boosted trees** — tabular champion; needs SHAP layer for trust.
4. **Neural nets** — only for text/images/sequences OR proven material uplift.

## Fair comparison protocol
- Identical CV folds across candidates (same random_state).
- Same feature preprocessing inside each pipeline (no leakage).
- Repeated CV (5×5) when differences are small; bootstrap CIs on headline metric.
- Report training + inference time next to accuracy.

## Escalation rule
Move up a rung ONLY IF gain > combined CI overlap AND complexity cost is acceptable.
"AUC went 0.843 → 0.847 with a 40× slower model" is a NO.

## Interpretability ladder
| Model | Explanation artifact |
|---|---|
| Linear | standardized coefficients |
| Tree ensemble | SHAP summary, dependence plots |
| Any | example-based: show 3 predictions with reasons |

## Practical defaults
Tabular + <10k rows → regularized linear first. Tabular + 10k–10M → LightGBM/XGBoost.
Text → pretrained transformer embeddings + linear head before anything fancier.
