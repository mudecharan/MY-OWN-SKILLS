---
name: bayesian-analysis-guide
description: Apply Bayesian reasoning to business problems — priors from history, posterior updates, credible intervals, Bayesian A/B decisions. Activate when data arrives sequentially, samples are small, or stakeholders think in probabilities not p-values.
---

# When to use
- Continuous monitoring of live experiments without peeking penalties
- Small-sample problems where frequentist intervals are too wide to act on
- Combining historical knowledge ("we've launched 20 similar features") with new evidence

# Process
1. **Frame as belief updating** — define the parameter of interest (conversion delta, churn probability, demand elasticity) and what "knowing" it would enable.
2. **Prior construction** — elicit from historical data (empirical Bayes over past campaigns/tests) or weakly-informative defaults; always run prior-sensitivity checks and report both skeptical and enthusiastic priors.
3. **Model & sample** — conjugate shortcuts where valid (Beta-Binomial, Normal-Normal); PyMC/Stan for hierarchical or complex likelihoods; posterior predictive checks for model fit.
4. **Decision quantities** — P(B>A), expected loss if wrong (the loss function matters more than the probability), highest-density interval, shrinkage estimates for small segments.
5. **Sequential stopping** — stop when expected loss < threshold; this is safe under continuous monitoring unlike naive p-value peeking.
6. **Communicate** — replace "not significant" with "there's a 73% chance B beats A; if wrong, we lose ~0.2% conversion" — then let the business decide.

# Inputs the skill needs
- Required: outcome data, decision at stake, cost of a wrong call
- Optional: historical comparable experiments for empirical-Bayes priors

# Output
- Fitted model code + posterior summaries/plots
- Decision statement in probability-and-loss terms
- Prior-sensitivity appendix

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/bayesian_ab.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/bayesian_practice_notes.md` - read before starting.

### assets/ - templates to fill and deliver
- `assets/bayesian_report_template.md` - Fill this template - it IS the deliverable format.
