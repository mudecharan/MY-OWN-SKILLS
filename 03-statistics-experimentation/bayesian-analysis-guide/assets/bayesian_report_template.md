# Bayesian Analysis Report — <question>

## 1. Decision frame
| Item | Value |
|---|---|
| Parameter of interest | |
| Decision the posterior informs | |
| Cost of a wrong call (loss function) | |
| Stop rule (expected-loss threshold) | |

## 2. Priors
| Prior | Distribution | Justification |
|---|---|---|
| Base / enthusiastic | Beta(1,1) or empirical-Bayes from __ past tests | |
| Skeptical | Beta(100+x, 100+n−x) | new variants must prove themselves |

## 3. Posterior results
- P(B > A): ____%
- Posterior means / 95% HDI: A = __ [__, __] · B = __ [__, __]
- Expected loss if choosing each arm:
  - choose A → ____
  - choose B → ____

## 4. Prior sensitivity
Verdict under base prior vs skeptical prior — do they agree? If not, why.

## 5. Plain-language decision statement
"There is a __% chance B beats A. If we're wrong, we expect to lose about __
<business units>. Recommendation: <stop and choose X / continue collecting>."

## Model diagnostics
- [ ] posterior predictive checks passed
- [ ] convergence (R-hat < 1.01) if MCMC used
