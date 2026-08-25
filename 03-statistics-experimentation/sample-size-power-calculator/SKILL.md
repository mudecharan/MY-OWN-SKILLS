---
name: sample-size-power-calculator
description: Compute sample sizes and statistical power for any study type — proportion/mean tests, chi-square, regression detection limits, surveys with clustering. Activate when someone asks "how many do we need?"
---

# When to use
- Designing surveys, experiments, or audits
- Reviewing underpowered research before trusting its conclusions
- Justifying data-collection budgets with numbers

# Process
1. **Parameterize** — estimand (proportion, mean difference, effect size d/f²), baseline values, alpha, power, tails, one-vs-two-sided.
2. **Compute** — closed-form formulas where valid (Cohen's tables, normal approximations); simulation-based power for complex designs (mixed models, cluster randomized, non-normal outcomes).
3. **Design corrections** — design effect for clustered sampling (1+(m−1)×ICC), finite population correction, attrition inflation (n_adj = n/(1−dropout)), multiple-comparison inflation if applicable.
4. **Sensitivity table** — produce grid: MDE achievable at given n AND n needed at given MDE; highlight the feasible frontier.
5. **Plain-language verdict** — "With N=X, you can reliably detect a Y% change; smaller effects would need Z more observations."
6. **Post-hoc honesty** — for completed studies, compute what was actually detectable instead of fake "observed power".

# Inputs the skill needs
- Required: study design type, primary comparison, baseline estimate
- Optional: budget-constrained max n (→ solve for achievable MDE instead)

# Output
- Sample-size calculation with formula/code shown
- Sensitivity grid (MDE × n × power)
- One-paragraph plain-language justification for stakeholders

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/sample_size.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/power_rules.md` - apply these rules; they override defaults

### assets/ - templates to fill and deliver
- `assets/power_record_template.md` - Fill this template - it IS the deliverable format.
