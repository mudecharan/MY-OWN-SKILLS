---
name: causal-inference-advisor
description: Choose and apply causal inference methods when randomization is impossible — DiD, synthetic control, matching, IV, regression discontinuity. Activate when a stakeholder asks "did X CAUSE the change?"
---

# When to use
- A policy/pricing/feature change rolled out to everyone at once
- Self-selection bias contaminates a naive comparison
- Post-hoc evaluation of a program's true impact

# Process
1. **Causal diagram first** — sketch the DAG: treatment, outcome, confounders, colliders, mediators. Identify the backdoor paths that must be blocked. Never adjust blindly for "everything".
2. **Method selection by setting**:
   - Before/after with clean parallel trends → Difference-in-Differences (+ event-study pre-trend test)
   - No control unit → Synthetic control / comparative interrupted time series
   - Rich covariates, ignorable assignment → Propensity score matching/IPW (+ balance diagnostics)
   - Sharp/fuzzy eligibility cutoff → Regression discontinuity
   - Valid instrument exists → IV/2SLS (test instrument strength)
3. **Assumption audit** — write down each method's key assumption, how it could fail here, and which sensitivity analysis applies (Rosenbaum bounds, placebo tests, leave-one-out).
4. **Estimate** — implement with robust SEs (clustered where grouping exists); report effect + CI in business units.
5. **Triangulate** — run ≥2 defensible methods; agreement raises confidence, disagreement demands explanation.

# Inputs the skill needs
- Required: treatment timeline & who/what got treated, outcome data, candidate confounders
- Optional: untouched comparison groups, eligibility rules

# Output
- DAG + assumption audit per candidate method
- Effect estimates with CIs from triangulated methods
- Plain-language causal claim with explicit confidence boundaries

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/causal_toolkit.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/assumption_categories.md` - read before starting.
- `references/method_selection_guide.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/causal_report_template.md` - Fill this template - it IS the deliverable format.
