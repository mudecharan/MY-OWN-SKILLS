# Sample Size & Power — Calculation Record

## Study parameters
| Parameter | Value | Source of estimate |
|---|---|---|
| Primary comparison | |
| Baseline (p1 or mean) | |
| MDE (smallest effect worth acting on) | |
| α / tails / power | |
| Expected dropout/attrition | |

## Result
- n per arm: ______ (formula/code shown below)
- Total: ______ · With attrition inflation: ______
- Feasible frontier:

| If n is fixed at… | Achievable MDE |
|---|---|
| 1,000 | |
| 5,000 | |
| 20,000 | |

## Plain-language verdict for stakeholders
"With N = ____, we can reliably detect a ____% change. Smaller effects would need
____ more observations, so we either accept the current resolution or extend the window."

## Design corrections applied
- [ ] design effect for clustering: DEFF = 1 + (m−1)×ICC = ____
- [ ] finite population correction
- [ ] attrition inflation: n / (1 − d)
- [ ] multiplicity adjustment if >1 primary comparison
