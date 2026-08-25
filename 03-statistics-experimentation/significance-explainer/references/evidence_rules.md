# P-Value & Evidence Communication Rules

## What a p-value IS and IS NOT
| Statement | Verdict |
|---|---|
| "P(data | null true)" | ✅ correct (roughly) |
| "Probability the hypothesis is true" | ❌ |
| "Probability results are due to chance" | ❌ |
| "Measure of effect importance" | ❌ |

## The CI is the star
A confidence interval contains everything a p-value says PLUS magnitude and precision.
Report format: `effect = X [95% CI: L, U]` — then interpret the interval's business meaning.

## Multiplicity corrections quick reference
| Situation | Correction |
|---|---|
| Few (<10) confirmatory comparisons, want zero false positives | Holm / Bonferroni |
| Many exploratory hypotheses, tolerate some false leads | Benjamini-Hochberg FDR |
| Pre-planned single primary metric | none needed |

## Evidence-to-action mapping (default policy)
| Adjusted result vs materiality bar | Recommended action |
|---|---|
| Significant AND ≥ MDE | ship |
| Significant but < MDE | don't claim victory; note real-but-tiny |
| Not significant, well-powered | no evidence; keep control (never "it's equal") |
| Not significant, underpowered | extend sample or declare inconclusive honestly |

## Fragile finding red flags
Result flips under: different test family, one outlier removed, one segment excluded,
one alternate period definition. Label fragile; do not headline it.
