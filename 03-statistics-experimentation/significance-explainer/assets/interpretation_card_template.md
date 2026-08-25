# Statistical Interpretation Card — <finding>

## Lead with the estimate (never the p-value)
> "The new flow converts at __% vs __% control (+__pp, 95% CI __ to __)."

## Two questions, answered separately
1. **Is there evidence of an effect?** → statistics (test, CI, p after correction)
2. **Is it big enough to matter?** → business judgment against the MDE

## Myth corrections applied to this analysis
| Claim made somewhere | Correction |
|---|---|
| "p = 0.07 means no effect" | Absence of evidence ≠ evidence of absence |
| "CIs overlap so no difference" | Overlap is not a valid test; run the comparison |
| "p < 0.001 = huge effect" | Significance ≠ magnitude; look at CI width |
| "not significant = groups are equal" | Underpowered tests can't confirm equality |

## Multiplicity audit
- Total comparisons explored (metrics × segments × periods): ____
- Correction applied: Holm / BH — adjusted results table attached
- Exploratory findings labeled as exploratory: ☐

## Robustness trio results
| Check | Alternative used | Conclusion held? |
|---|---|---|
| Test family | Mann-Whitney vs t-test | |
| Outlier treatment | winsorized P99 | |
| Subgroup definition | excl. top segment | |

## Action recommendation
Strong evidence + material size → ship · Moderate → pilot · Weak/null → state
what n WOULD answer it; do not declare equality.
