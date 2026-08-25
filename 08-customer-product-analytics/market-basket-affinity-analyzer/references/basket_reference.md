# Market Basket Reference

## Metric meanings (keep straight)
| Metric | Question | Threshold |
|---|---|---|
| support P(A∩B) | how common is the pair at all? | ≥0.5% of baskets to matter |
| confidence P(B\|A) | if A in basket, is B too? | ≥15% for actionable |
| lift P(A∩B)/(P(A)P(B)) | REAL affinity beyond co-popularity | **>1.3 useful; ≤1 = discard** |

Lift is the only honest one — high-confidence rules on popular items are usually just popularity.

## Basket construction decisions
- Grain: order vs session vs visit-window (returns trips split orders!)
- Filter: staff/test accounts, bulk buyers (B2B distorts retail affinities)
- Split analysis halves: a rule strong in H1 but not H2 is seasonal artifact or noise.

## Complement vs substitute
Complements: bought TOGETHER (positive lift).
Substitutes: rarely together BUT same category + similar buyers → detect via
"basket contains A XOR B" frequency. Substitutes inform assortment, not bundles.

## Application mapping
| Placement | Rule type used | Measure of success |
|---|---|---|
| product-page "frequently bought together" | top conf A→B complements | attach rate |
| checkout add-on | small-ticket complements | incremental units |
| email cross-sell | segment-aware rules | incremental margin |
| bundle pricing | strongest stable pairs | bundle must beat sum-of-parts margin |

## Validate with experiments
Placement changes get A/B tests; success = incremental MARGIN, never clicks.
