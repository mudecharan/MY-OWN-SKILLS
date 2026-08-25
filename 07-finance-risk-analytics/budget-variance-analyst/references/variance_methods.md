# Variance Analysis Method Reference

## Materiality gates
Investigate only variances passing BOTH: >X% of line AND >$Y absolute.
Without both, you drown in noise or miss big-but-quiet lines.

## Volume–price–mix decomposition (revenue)
Given: units actual/budget (Qa/Qb), price actual/budget (Pa/Pb):
| Effect | Formula | Question it answers |
|---|---|---|
| Volume | (Qa−Qb) × Pb | did we sell more/less? |
| Price | Qa × (Pa−Pb) | did we charge more/less? |
| Mix | residual when selling multiple products at different margins | did the SALES MIX shift toward cheaper items? |

Mix = the effect people forget. Revenue can hit budget with fewer units sold
because mix shifted premium — and that's a very different problem.

## Rate vs usage (costs)
| Effect | Formula |
|---|---|
| Rate | actual quantity × (actual rate − std rate) — did unit cost change? |
| Usage | (actual qty − std qty) × std rate — did consumption change? |

## Timing vs permanent
Timing variances reverse next period (billing lag) — track them in a reversal ledger.
"Timing" without a stated reversal date is an unexplained variance wearing a costume.

## Re-forecast method
Full-year = actuals-to-date + remaining-year projection where:
projection = run-rate adjusted for known one-offs + pipeline/seasonality.
Compare re-forecasts to original budget over time → measures PLANNING quality,
which is a separate (and fairer) conversation than performance.
