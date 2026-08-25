# Association Methods Reference

## Method routing table
| Pair type | Method | Notes |
|---|---|---|
| numeric × numeric (linear) | Pearson r | sensitive to outliers — check scatter |
| numeric × numeric (monotonic) | Spearman ρ | robust; big Pearson–Spearman gap ⇒ nonlinearity |
| ordinal × ordinal | Kendall τ-b | better with ties/small n |
| binary × numeric | Point-biserial | = Pearson with 0/1 coding |
| categorical × categorical | Cramér's V (chi²-based) | bias-corrected version preferred |
| categorical → numeric | Correlation ratio η | effect of group membership |

## Strength interpretation (common convention)
| \|r\| / Cramér's V | Label |
|---|---|
| < 0.10 | negligible |
| 0.10–0.30 | weak |
| 0.30–0.50 | moderate |
| > 0.50 | strong |

## Multicollinearity thresholds
- **VIF > 5** → investigate the variable cluster
- **VIF > 10** → act: drop, combine into index, or use regularization/PCA
- Also check pairwise |r| > 0.8 as a fast pre-filter

## Causation guardrails
Before reporting "X is associated with Y", list:
1. Plausible confounders (Z causes both).
2. Reverse causation possibility.
3. Selection effects in how data was collected.
4. A lag test if time ordering exists (does X at t predict Y at t+1?).

## p-value caution
With large n everything becomes "significant" — lead with effect size, use p only as noise filter.
