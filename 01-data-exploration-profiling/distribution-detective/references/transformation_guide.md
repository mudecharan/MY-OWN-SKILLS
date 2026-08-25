# Transformation & Distribution Guide

## When each transform helps
| Transform | Fixes | Watch out |
|---|---|---|
| log / log1p | right skew, heavy right tail, multiplicative processes | zeros (use log1p), negatives; interpretation changes |
| sqrt | moderate right skew (counts) | less powerful than log for extreme skew |
| Box-Cox | finds optimal power λ (positive data only) | λ must be reported for reproducibility |
| Yeo-Johnson | like Box-Cox but handles zeros/negatives | slightly harder to explain |
| Quantile (rank-Gauss) | forces normal shape | distorts distances; per-batch instability in production |
| Reciprocal | very strong right tail | fragile near zero |

## Choosing the summary statistic
| Shape | Report |
|---|---|
| approx symmetric | mean ± std |
| right-skewed (money, counts, durations) | **median + IQR** or trimmed mean |
| bimodal | split by the hidden segment first — never a single center |

## Test selection after checking shape
- Normal-ish + equal variances → t-test / ANOVA
- Skewed → Mann-Whitney U / Kruskal-Wallis
- Any shape, want CIs on median/mean → Bootstrap (always valid)
- Comparing tails specifically → quantile regression

## Modality = mixture
Bimodal output usually means two populations share the column. Hunt the splitter:
device, plan tier, region, new-vs-returning. Re-plot within segments before transforming anything.

## Pareto check
Report what % of total value the top 1% and 5% carry.
If top 5% > 50%, means are marketing fiction — use medians and segment views.
