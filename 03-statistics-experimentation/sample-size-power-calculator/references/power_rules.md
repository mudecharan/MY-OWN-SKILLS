# Power & Sample Size Rules

## The five knobs
n, effect size (MDE), α, power, σ (noise). Fix any four; the fifth is determined.
Business usually fixes MDE ("we only care if it moves ≥2%") and budget (n) → solve for achievable power honestly.

## Effect size conventions (Cohen)
| d | Label | Rough meaning |
|---|---|---|
| 0.2 | small | needs big samples |
| 0.5 | medium | typical behavioral intervention |
| 0.8 | large | rare in field experiments |

## Cluster randomized designs
Multiply n by design effect: **DEFF = 1 + (m − 1) × ICC** where m = cluster size.
Clinics/schools/stores as units → ICC of 0.05 with clusters of 50 doubles required n.

## Survey sampling
- Proportions: worst-case p=0.5 maximizes n: n = 1.96²·0.25 / MOE²
- Finite population correction when sample >5–10% of population.

## Post-hoc power is banned
"Observed power" computed from the observed effect adds no information and misleads.
For null results report instead: "the study could have detected effects ≥ X with 80% power."

## Attrition is not optional math
Real studies lose 10–30%. Plan n_final = n_required / (1 − dropout).
