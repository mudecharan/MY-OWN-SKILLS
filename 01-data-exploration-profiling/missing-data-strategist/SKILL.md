---
name: missing-data-strategist
description: Diagnose why data is missing (MCAR/MAR/MNAR) and prescribe the statistically correct treatment — not just "fill with median". Activate whenever nulls exceed ~2% on analysis-critical columns.
---

# When to use
- A critical column has significant gaps and dropping rows would bias results
- Model training fails or degrades due to NaNs
- You must defend an imputation choice in review

# Process
1. **Quantify** — missingness count/% per column, per segment, per time period; visualize the missingness matrix to spot block patterns.
2. **Mechanism diagnosis** — test MCAR via Little's test / group comparisons; check if missingness in column A predicts values in column B (MAR signal); suspect MNAR when the missing thing relates to itself (e.g., high earners hide income). State the verdict explicitly with evidence.
3. **Treatment decision tree**:
   - MCAR + <5% → listwise deletion acceptable
   - MAR → model-based imputation (MICE, KNN, missForest)
   - MNAR → imputation will bias; flag, analyze observed-only with caveats, or collect better data
   - Time series → forward-fill only within short gaps; never across structural breaks
4. **Imputation execution** — fit on TRAIN split only when modeling; add `was_missing` indicator columns where missingness itself is informative.
5. **Uncertainty propagation** — for key estimates use multiple imputation (m=5+) and pool results; report imputation-driven variance.
6. **Validation** — artificially mask 10% of complete values, impute, measure recovery error; report it.

# Inputs the skill needs
- Required: dataset, columns needing treatment, downstream use case (descriptive stats vs ML vs inference)
- Optional: domain knowledge about why data goes missing

# Output
- Missingness diagnostic report (matrix plot, mechanism verdict with evidence)
- Implemented treatment pipeline (reproducible function/notebook cells)
- Validation metrics showing imputation quality; caveats section for the final report

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/imputation_lab.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/imputation_decision_tree.md` - consult to choose the correct branch before acting
- `references/quality_thresholds.md` - read before starting.

### assets/ - templates to fill and deliver
- `assets/missingness_report_template.md` - Fill this template - it IS the deliverable format.
