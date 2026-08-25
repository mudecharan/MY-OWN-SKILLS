# Anomaly Detection Spec — <metric/system>

## Normal profile
| Component | Finding |
|---|---|
| Level & trend | |
| Seasonality (period) | |
| Residual std (MAD-scaled) | |
| Known event calendar to suppress | |

## Detector configuration
| Parameter | Value | Rationale |
|---|---|---|
| Method | STL residual + MAD-z | |
| z threshold | | from calibration sweep |
| persistence | | kills single-point noise |

## Calibration backtest
| Threshold | Precision | Recall | Alerts/day | Verdict |
|---|---|---|---|---|

Selected operating point: ____ (justification: alert volume sustainable)

## Alert routing
| Severity | Condition | Channel | Response SLA | Runbook link |
|---|---|---|---|---|

## Feedback loop
Responder verdicts logged in ____ · re-tune cadence: monthly
