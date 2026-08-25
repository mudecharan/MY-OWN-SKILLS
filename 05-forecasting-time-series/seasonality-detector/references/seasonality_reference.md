# Seasonality & Calendar Effects Reference

## Verifying the true period
1. ACF peaks at the candidate lag (7 for daily data, 12 for monthly).
2. Periodogram/Fourier power as cross-check.
3. Group means by day-of-week / month — do the numbers match the ACF story?
Beware: 4-4-5 retail calendars make "monthly" seasonality shift with the calendar.

## Seasonal strength (Wang–Smith–Hyndman)
`Fs = max(0, 1 − Var(remainder) / Var(seasonal + remainder))`
| Fs | Interpretation |
|---|---|
| < 0.2 | weak — probably ignore |
| 0.2–0.6 | moderate — include but don't over-tune |
| > 0.6 | strong — must be modeled or adjusted |

## Calendar artifacts ≠ seasonality
- Working-day counts (Feb is short; some months have 2 fewer selling days)
- Holiday shifts (Easter moves; Ramadan moves a lot)
- Payday effects (spikes at month end / specific weekdays)
Handle via regressors or trading-day adjustment, not the seasonal component.

## Evolving seasonality
Run STL on rolling windows; if Friday's premium shrinks over years, you have
non-stationary seasonal pattern → use dynamic methods, not fixed indices.

## What to do per use case
| Use case | Action |
|---|---|
| Reporting KPIs | show seasonally-adjusted series next to raw |
| Forecasting | explicit seasonal terms |
| Anomaly detection | detect on seasonally-adjusted residuals |
