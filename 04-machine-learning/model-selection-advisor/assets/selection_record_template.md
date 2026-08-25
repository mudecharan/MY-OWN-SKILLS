# Model Selection Decision Record — <project>

## Constraints inventory
| Constraint | Value | Rules out |
|---|---|---|
| Interpretability requirement | | deep nets, ensembles without SHAP layer |
| Scoring latency budget | | large ensembles, heavy preprocessing |
| Retrain frequency / drift speed | | anything needing long retraining |
| Team maintenance skills | | exotic frameworks |
| Serving infra available | | GPU models etc. |

## Baseline ladder results (identical splits!)
| Rung | Model | Metric ± CI | Fit time | Infer ms | Verdict |
|---|---|---|---|---|---|
| 0 rules/average | | | | | |
| 1 linear/logistic (reg.) | | | | | |
| 2 GBT (xgboost/lightgbm) | | | | | |
| 3 neural / other | only if justified | | | | |

## Escalation justification (if used)
- Gain over rung below exceeds bootstrap CI overlap? ☐ evidence attached
- Complexity cost worth it? ☐

## Winner & rationale
Selected model: ____
Why it won: ____
Trade-offs accepted: ____

## Interpretation artifact for stakeholders
- [ ] linear: standardized coefficient table
- [ ] trees: SHAP summary + dependence plots
- [ ] stakeholder sign-off on explanation: ☐
