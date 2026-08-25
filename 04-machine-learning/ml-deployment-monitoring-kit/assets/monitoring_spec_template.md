# Model Monitoring Spec — <model vN>

## Reference distributions (from training data — attach artifact hash)
| Feature | PSI alert threshold (>0.25 = investigate) | KS p-value floor |
|---|---|---|

## Alert triad
| Layer | Metric | Window | Threshold | Severity |
|---|---|---|---|---|
| Data drift | PSI per feature vs training ref | daily | >0.25 warn / >0.5 page | P2/P1 |
| Prediction drift | score distribution shift (PSI) | daily | >0.25 | P2 |
| Performance | delayed-label AUC / MAE once labels mature (lag __ days) | weekly | < __ floor | P1 |
| Ops | error rate, latency p95, throughput | realtime | err>1%, lat>__ms | P0 |

## Rollout plan
- [ ] Shadow mode 2–4 weeks: agreement with current process logged; no actions taken
- [ ] Progressive: 5% → 25% → 100% (or champion/challenger)
- [ ] Auto-rollback triggers defined: ____

## Retraining policy
| Trigger | Rule |
|---|---|
| Drift | any feature PSI > 0.5 sustained 3 days |
| Calendar | every __ months regardless |
| Performance | live metric below floor for 2 weeks |

Retrain procedure: fresh window → same evaluation gates as v1 → human sign-off → promote.
Never auto-promote.

## Runbook
- Kill switch: ____
- Last-known-good artifact location + data hash: ____
- On-call owner: ____
