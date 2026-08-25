---
name: correlation-radar
description: Systematic bivariate and multivariate relationship scanning — Pearson/Spearman/Kendall, categorical associations (Cramér's V), correlation-vs-causation checks, and multicollinearity flags. Activate during feature selection or hypothesis hunting.
---

# When to use
- Hunting for drivers of a KPI across dozens of candidate variables
- Feature selection before regression/ML (multicollinearity kills interpretability)
- Validating that a suspected driver actually correlates with the outcome

# Process
1. **Variable typing** — classify every pair context: numeric×numeric, numeric×categorical, categorical×categorical, ordinal cases.
2. **Method routing** — Pearson (linear, normal-ish), Spearman (monotonic/outlier-robust), Cramér's V (categorical), point-biserial (binary×numeric); correlation ratio for categorical→numeric.
3. **Full-matrix sweep** — compute all applicable pairs; produce sorted league table of |association| with p-values and effect interpretation (negligible/weak/moderate/strong).
4. **Nonlinearity check** — compare Pearson vs Spearman gaps; large gap = nonlinear relationship worth plotting (scatter with LOESS).
5. **Multicollinearity audit** — VIF on candidate predictors; flag VIF>5 (investigate) and >10 (act).
6. **Causation guardrail** — for top pairs, list plausible third-variable explanations and lag tests before anyone says "drives".
7. **Shortlist** — recommend top relationships to visualize/model next.

# Inputs the skill needs
- Required: dataset, target variable (if driver-hunting)
- Optional: known confounders, minimum practical effect size

# Output
- Association league table (pair, method, coefficient, p-value, strength label)
- Multicollinearity report with VIFs and drop/combine recommendations
- Scatter/LOESS plots for the top 10 non-linear-suspect pairs

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/correlation_explorer.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/correlation_sweep.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/association_methods.md` - read before starting.

### assets/ - templates to fill and deliver
- `assets/association_league_table_template.md` - Fill this template - it IS the deliverable format.
