# CLV Modeling Reference

## Definition discipline (get sign-off in one sentence)
"CLV = expected future MARGIN from a customer over __ months, discounted at __%."
Margin not revenue — revenue-based LTV overstates value by the entire COGS.
State whether it's total-lifetime (theoretical) or fixed-horizon (practical).

## Method ladder
| Rung | Method | When |
|---|---|---|
| 1 | Cohort curves: cumulative margin per customer by acquisition month | always; reveals saturation point → pick horizon |
| 2 | Historic average × survival decay | quick estimates, non-contractual |
| 3 | BG/NBD + Gamma-Gamma (lifetimes lib) | contractual or repeat-purchase businesses; needs only RFM inputs |

## BG/NBD validation
Hold out last 90 days: predict purchases in holdout from data before it;
compare predicted vs actual by decile. Calibrated by decile = trustworthy.

## Decision integrations
1. **LTV:CAC by channel** — kill channels below threshold (commonly 3:1); watch for
   channel mix shifting cohort quality over time.
2. **Early-life indicators** — features of first 30 days that predict top-CLV decile
   (first-order value, category breadth, activation speed) → target lookalikes.
3. **Segmentation input** — forward-CLV beats historic revenue for tiering.

## Caveats to state
Non-contractual churn is unobserved → model assumes it; margin data quality dominates everything.
