# Forecast Method Guide

## Non-negotiables
1. **Benchmarks first**: seasonal-naive and drift baselines. Any model not beating them adds noise, not value.
2. **Rolling-origin backtest only.** Never random-split a time series.
3. **Quantiles, not points** — planners need P10/P90 for safety stock and risk.

## Method chooser
| Data situation | Start with |
|---|---|
| Short series (<2 seasons), stable | ETS / simple exponential smoothing |
| Clear season + level/trend | Holt-Winters (ETS additive/multiplicative) |
| Many related series (SKU×store) | Global GBT on lags/calendar features or hierarchical reconciliation |
| Strong promo/event drivers | ARIMAX / regressors in decomposable models |
| Intermittent demand (sparse counts) | Croston's SBA |

## Hierarchy reconciliation
Forecast every level independently → store sums ≠ national.
Reconcile bottom-up, top-down, or MinT; publish ONE coherent set.

## Accuracy vocabulary (report MASE, never MAPE alone)
| Metric | Use |
|---|---|
| MAE | plain average error |
| MASE | error vs naive benchmark (>1 = worse than naive!) |
| RMSSE | like MASE, penalizes big misses |
| Bias (mean error) | systematic over/under-forecast — worse than random noise |

## Events & outliers
Promos/holidays → explicit regressors. One-off spikes → adjust for TRAINING,
never silently delete from history shown to stakeholders.

## Operations
Publish forecast vs actual weekly; track bias by segment; retire models that
drift above 1.0 MASE for 4 consecutive weeks.
