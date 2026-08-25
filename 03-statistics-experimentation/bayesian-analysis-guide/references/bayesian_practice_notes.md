# Bayesian Practice Notes

## Why expected loss, not P(B>A)
P(B>A)=80% sounds decisive until you ask "what's the cost if wrong?"
Expected loss combines probability AND magnitude — it's the number that should drive stopping.
Stop when min(E[loss]) < threshold set from the business cost of a bad rollout.

## Choosing priors honestly
1. **Empirical Bayes first**: fit a distribution over effects of past similar experiments.
   That IS your informed prior — no philosophy required.
2. Weakly-informative defaults otherwise (Beta(1,1), Normal(0, 10·σ)).
3. ALWAYS report the skeptical-prior view alongside; if conclusions flip,
   you don't have a result, you have a prior fight.

## Conjugate shortcuts (no MCMC needed)
| Likelihood | Prior | Posterior |
|---|---|---|
| Binomial conversions | Beta(α, β) | Beta(α + x, β + n − x) |
| Normal mean (known σ) | Normal(μ₀, τ²) | precision-weighted Normal |
| Poisson counts | Gamma(α, β) | Gamma(α + Σx, β + n) |

## Sequential monitoring
Unlike naive p-value peeking, expected-loss thresholds are safe to check daily.
This is the main operational reason teams switch to Bayes for A/B testing.

## When frequentist is still right
Regulated claims, one-shot confirmatory trials with pre-registered α — stick to NHST there.
