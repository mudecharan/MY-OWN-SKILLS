# Pricing Analysis — <product/market>

## 1. Realized-price forensics
| Segment | List price | Avg realized price | Discount leakage % | Volume response to discounts? |
|---|---|---|---|---|

Discount audit conclusion: who gets discounts, and does volume actually follow?

## 2. Elasticity estimates (with identification caveats)
| Segment | Elasticity | 95% CI | Identification source (test/region/cost event) | Caveat |
|---|---|---|---|---|
NEVER naive price-vs-quantity correlation — prices and demand co-move with season.

## 3. Promotion audit
| Promo | Incremental lift vs baseline | Pull-forward effect | Pantry loading | ROI |
|---|---|---|---|---|

## 4. Scenario engine (margin × volume)
| Move | Volume change (from elasticity) | Margin impact | Net profit impact |
|---|---|---|---|
| +5% price | | | |
| −5% discount tightening | | | |
| new tier introduction | | | |

## 5. Validation test design
- Split unit: geography / cohort ____
- Success metric + guardrails declared up front: ____
- Duration & power: ____

## Recommendation
Per-segment price direction with confidence bounds; what we still don't know and the test that will tell us.
