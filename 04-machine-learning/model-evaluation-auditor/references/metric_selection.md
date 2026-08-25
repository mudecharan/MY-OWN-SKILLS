# Metric Selection by Problem Shape

| If the decision needs... | Use | Ignore |
|---|---|---|
| Top-k list (fraud queue, recommendations) | Precision@k, PR-AUC | ROC-AUC (misleading on imbalance) |
| Calibrated probabilities (pricing, expected loss, budgets) | Brier score + reliability curve | AUC alone |
| Ranking quality of full list | ROC-AUC as coarse check | accuracy |
| Quantile estimates / asymmetric costs | Pinball loss, cost-weighted threshold sweep | RMSE |
| Count forecasting with intermittent zeros | MAE + bias split, MASE | R² |

## Calibration fix ladder
1. Predicted-vs-actual decile plot: monotone but offset → Platt scaling.
2. Non-monotone distortion → isotonic regression (needs >~5k calibration rows).
3. Always fit recalibration on a SEPARATE fold from training.

## Bootstrap CIs on metrics
Resample held-out rows ~1000×; report 2.5/97.5 percentiles.
Model A "beats" B only if their CIs don't overlap meaningfully.

## Slice review minimum set
Region · device/channel · tenure cohort · top/bottom value quartile ·
any legally protected attribute relevant to fairness review.

## The one-question audit
"Would this model's predictions, used at THIS threshold on REAL data, make money?"
If the eval can't answer that, it isn't done.
