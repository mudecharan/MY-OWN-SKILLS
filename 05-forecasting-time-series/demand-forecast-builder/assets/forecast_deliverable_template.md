# Forecast Deliverable — <series/process>

## Backtest evidence
| Method | MAE | MASE | Bias | Verdict |
|---|---|---|---|---|
| seasonal_naive | | 1.00 (ref) | | benchmark |
| naive_drift | | | | benchmark |
| <model> | | | | selected if MASE<1 |

Backtest design: rolling origin, __ folds, horizon __ days.

## Forecast (P10/P50/P90) at required granularity
| Period | P10 | P50 | P90 |
|---|---|---|---|

## Reconciliation check
Sum of lower levels matches total after reconciliation: ☐

## Assumptions & event overlay
- Promotions included as regressors: ____
- Known one-offs excluded from training: ____
- Structural changes assumed to persist: ____

## Consumer guidance
- Inventory planner: use P90 for reorder quantity where stockout cost is high.
- Finance: use P50; quote range, not point.

## Accuracy tracking plan
Weekly actual-vs-forecast review; bias alarm when mean error > __% of level for 3 weeks.
