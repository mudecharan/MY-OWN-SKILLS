# Seasonality Findings — <metric>

## Verified periods
| Candidate period | Evidence (ACF peak r) | Confirmed? |
|---|---|---|

## Seasonal strength
Fs = ____ → verdict: model it / monitor only

## Seasonal profile (index vs mean level = 100)
| Day/Month | Index | Note |
|---|---|---|

## Calendar effects found
| Effect | Nature | Handling chosen |
|---|---|---|
| e.g., working-day count | Feb short | trading-day adjusted |
| e.g., holiday X | date shifts yearly | regressor |

## Stability check
Seasonal pattern stable across years? Yes / No (rolling STL evidence: ____)
If No → dynamic handling required.

## Recommendation per use case
- Reporting: seasonally-adjusted view ☐
- Forecasting: seasonal terms with period ____ ☐
- Anomaly detection: operate on adjusted residuals ☐
