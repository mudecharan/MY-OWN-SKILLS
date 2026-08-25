---
name: ab-test-designer
description: End-to-end A/B test design and execution — hypothesis, MDE, sample size, randomization, guardrails, run-time discipline, and decision rules. Activate before anyone launches an experiment.
---

# When to use
- Product/marketing wants to "try something and see"
- A past test was inconclusive and you suspect design flaws
- Planning the experiment roadmap for a quarter

# Process
1. **Hypothesis charter** — one-sentence causal claim ("changing X will move Y because Z"), primary metric, decision deadline.
2. **Feasibility math** — baseline rate, minimum detectable effect (negotiate: smallest effect worth acting on), alpha=0.05, power=0.8 → required n per arm; compute expected runtime from traffic; if >4 weeks, escalate options (higher-risk-tolerant decision, covariates, different unit).
3. **Randomization plan** — unit of randomization (user, not session), hashing/salt strategy, SRM (sample-ratio mismatch) check spec, contamination/leakage audit.
4. **Metrics tree** — 1 primary, ≤5 secondary, ≥2 guardrails (latency, unsubscribe, error rates) with per-metric judgment thresholds set BEFORE launch.
5. **Run discipline** — no peeking decisions without sequential correction; fixed-horizon or group-sequential declared up front; novelty-effect monitoring by cohort week.
6. **Decision memo** — result, confidence interval in business units, segment heterogeneity notes, ship/no-ship/iterate recommendation with expected annualized impact.

# Inputs the skill needs
- Required: metric baseline + variance, available traffic/unit volume
- Optional: historical test results, business risk appetite

# Output
- Test design document (charter, power calc, randomization spec)
- Analysis notebook template with SRM/guardrail checks pre-coded
- Decision memo at conclusion

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/ab_test_analyzer.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/ab_test_tool.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/ab_test_design_guide.md` - read before executing the Process
- `references/experiment_pitfalls.md` - read before starting.

### assets/ - templates to fill and deliver
- `assets/ab_test_report_template.md` - Fill this template - it IS the deliverable format.
- `assets/test_charter_template.md` - Fill this template - it IS the deliverable format.
