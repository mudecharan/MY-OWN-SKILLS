---
name: demand-forecast-builder
description: Build operational demand forecasts with hierarchical reconciliation, uncertainty bands, and accuracy tracking. Activate for inventory, staffing, revenue, or capacity forecasting needs.
---

# When to use
- Planning inventory, headcount, or budgets by period/region/product
- Finance asks for a defensible next-quarter number
- Replacing spreadsheet forecasts that are always wrong

# Process
1. **Forecast object definition** — what level (SKU? store? total?), horizon, frequency, and the decision that consumes it (order quantity → need quantiles, not means).
2. **Baseline benchmarks FIRST** — naive (last value), seasonal-naive (same period last year), moving average; any model must beat these or it's noise.
3. **Model tournament** — backtest with rolling-origin cross-validation (never random splits); candidates: ETS, SARIMA, Prophet-style decomposable, gradient boosting on lag/calendar features; compare via MASE/RMSSE on multiple holdout windows.
4. **Hierarchy reconciliation** — forecast bottom levels and total independently; reconcile (MinT or proportional) so store sums match national — otherwise planners won't trust it.
5. **Uncertainty quantification** — prediction intervals; report P10/P50/P90; for inventory derive safety stock from the quantile gap.
6. **Event overlay** — promotions/holidays/outliers handled via explicit regressors, not silently absorbed.
7. **Accuracy ops** — publish weekly forecast vs actual with bias tracking; systematic bias is worse than random error.

# Inputs the skill needs
- Required: historical series (≥2 seasonal cycles), forecast level & horizon
- Optional: promo/event calendar, hierarchy definitions

# Output
- Backtested model comparison table (MASE vs benchmarks)
- Production forecast with P10/P50/P90 at required granularity
- Accuracy tracking report template

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/backtest_forecast.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/forecast_method_guide.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/forecast_deliverable_template.md` - Fill this template - it IS the deliverable format.
