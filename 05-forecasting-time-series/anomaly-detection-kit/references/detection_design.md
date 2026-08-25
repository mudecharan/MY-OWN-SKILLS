# Anomaly Detection Design Reference

## Define "normal" before detecting anything abnormal
Profile: level · trend · seasonality · typical variance.
The detector operates on the residual after removing these.

## Method by data shape
| Metric behavior | Method |
|---|---|
| Flat level, no season | robust z-score (MAD-based; immune to outliers poisoning the baseline) |
| Daily/weekly season | STL residuals + MAD bands |
| Correlated metric group | multivariate: isolation forest / Mahalanobis — catches "each metric fine, combination weird" |
| Streaming | EWMA with adaptive control bands |

## Threshold calibration protocol
1. Inject synthetic anomalies (scale spikes 1.5–2×) OR use labeled incident history.
2. Sweep z-threshold × persistence; record precision/recall and daily alert volume.
3. Pick the operating point where alerts/day ≤ what on-call actually handles (usually ≤3).
4. Report the detector's own precision/recall like any classifier.

## Alert design rules
- Persistence ≥2 consecutive breaches for point metrics.
- Suppress during known events (Black Friday is not an anomaly).
- Every alert links a runbook; severity tiers (P0 page / P1 same-day / P2 weekly review).
- Log responder verdicts (true/false positive); re-tune monthly.

## Retirement rule
A detector with zero true hits in 6 months is either perfect or useless — investigate which.
