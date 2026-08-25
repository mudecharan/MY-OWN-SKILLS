# Causal Inference Method Selection Guide

## Step 0 — always: draw the DAG
List: treatment T, outcome Y, every confounder Z (causes both), colliders
(caused by both — NEVER adjust for these), mediators (adjusting kills the effect you want).

## Method chooser
| Setting | Method | Key assumption | How to probe it |
|---|---|---|---|
| Before/after with a clean control group, parallel trends plausible | Difference-in-Differences | trends would've moved together anyway | event-study plot of pre-period coefficients |
| Single treated unit, no control | Synthetic Control / comparative ITS | donor pool spans counterfactual | placebo tests on untreated units |
| Rich covariates + assignment ignorable | Propensity matching / IPW | no unobserved confounding | standardized bias < 0.1 after match; Rosenbaum bounds |
| Sharp eligibility cutoff (score ≥ X) | Regression Discontinuity | units near cutoff comparable | McCrary density test; covariate balance at cutoff |
| Valid instrument available (affects T, not Y directly) | IV / 2SLS | exclusion restriction (untestable!) | first-stage F > 10; over-ID test if >1 instrument |

## Triangulation protocol
Run at least TWO defensible methods. Same answer → confidence ↑.
Different answers → write down which assumption each method leans on and argue which is weaker HERE.

## Reporting standard
- Effect in business units with CI.
- Assumption audit table (assumption | could it fail here? why | sensitivity result).
- Never the bare word "caused" without this scaffolding.
