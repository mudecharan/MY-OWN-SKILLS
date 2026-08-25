---
name: distribution-detective
description: Deep univariate distribution analysis — shape, modality, skew, heavy tails, and correct transformation choices. Activate before statistical tests, modeling, or setting thresholds on any continuous variable.
---

# When to use
- Revenue, spend, session-time style variables that are never normal
- Choosing summary stats (mean lies with skewed data)
- Pre-processing decisions for models that assume normality or scale sensitivity

# Process
1. **Shape profile** — histogram with sensible binning (Freedman–Diaconis), KDE overlay, skewness, kurtosis, Shapiro/K-S normality test where meaningful.
2. **Modality check** — bimodal/multimodal shapes usually hide distinct populations; try separating by candidate segments and replot.
3. **Tail analysis** — QQ-plots vs normal and lognormal; quantify what % of total value sits in the top 1%/5% (Pareto check).
4. **Transformation lab** — fit and compare log, sqrt, Box-Cox, Yeo-Johnson, quantile transforms; pick using skew reduction AND interpretability trade-off.
5. **Discretization advice** — if binning helps communication, suggest data-driven bins (quantile or k-means), never arbitrary round numbers alone.
6. **Stat consequences** — state explicitly which central tendency to report, which test family is valid (parametric vs non-parametric), whether robust/Bootstrap methods are needed.

# Inputs the skill needs
- Required: numeric variable(s) and their business meaning
- Optional: segments to test for mixture distributions, downstream model requirements

# Output
- Distribution profile per variable (plots + stats + normality verdict)
- Recommended transformation with before/after evidence
- Reporting guidance card: correct statistic, correct test, tail-risk notes

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/distribution_profiler.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/distribution_summary.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/transformation_guide.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/distribution_profile_template.md` - Fill this template - it IS the deliverable format.
