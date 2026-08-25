# Pricing Analytics Reference

## Elasticity estimation without experiments
Exploit NATURAL price variation:
- regional price lists (same product, different markets)
- cost pass-through events (VAT change, input-cost spike)
- staggered price increases across cohorts
Estimate log(Q) = α + ε·log(P) + fixed effects (region × time) + seasonality.
Fixed effects absorb confounders; WITHOUT them, elasticity estimates are garbage.

## Elasticity decision math
| |ε| vs 1 | Meaning | Price move direction |
|---|---|---|---|
| < 1 inelastic | volume barely responds | raise price → margin up |
| > 1 elastic | volume responds strongly | cutting price can grow profit IF margin structure allows |
Profit-maximizing markup ≈ ε/(ε−1) for |ε|>1 — sanity-check recommendations against it.

## Promotion measurement traps
- Pull-forward: sales borrowed from next period, not incremental
- Pantry loading: consumers stockpile; no true demand increase
- Baseline must come from matched control stores/cohorts, not pre-period average

## Discount leakage audit
Realized = list − all discounts. Quantify by segment and sales rep.
Discounts uncorrelated with volume won = pure margin giveaway.

## Always end with a test
Elasticities from observational data are hypotheses. Design a geo/cohort split
price test, declare success metrics up front, then roll out what wins.
