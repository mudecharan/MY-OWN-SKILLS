# Trend Analysis Reference

## The noise-floor rule
A "trend" is only evidence if the per-period movement exceeds typical week-over-week
volatility over a sufficient window. Rule of thumb: need ≥8–12 periods before any
slope claim, and the slope should exceed ~2× the WoW standard error.

## Decomposition
STL (robust) separates level / trend / seasonal / remainder.
Report the TREND component — stakeholders looking at raw series see seasonality
and call it growth or decline.

## Change-point detection options
| Method | Strength |
|---|---|
| CUSUM | simple, streaming-friendly |
| PELT (ruptures lib) | principled, multiple breaks, cost function choice |
| Bayesian online changepoint | probabilistic, real-time |

Every detected break gets a business-cause hypothesis (launch? price change?
market event?) with dates matched. Unexplained breaks stay labeled unexplained.

## Simpson's paradox guard
Aggregate trends can reverse within segments. Before headline claims:
recompute trend per major segment; note divergent directions.

## Extrapolation honesty
- Linear projection valid 1–2 periods at most without justification.
- Always publish base/bull/bear bands; widen uncertainty with √horizon.
- Never extrapolate across a structural break using pre-break slope.

## Verdict language
"Real trend" = slope significant vs noise floor + survives segment checks +
consistent direction after seasonal adjustment. Anything less: "movement consistent with noise."
