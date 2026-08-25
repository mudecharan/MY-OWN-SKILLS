# Distribution Profile — <dataset>

## Per-variable cards
### Variable: <name>
- Business meaning: ____
- n, missing: ____
- Shape: skew __ · kurtosis __ · normality test verdict: __
- Modality: unimodal / multimodal → suspected splitter segment: ____
- Tail: top 5% of rows carry __% of total value (Pareto flag: yes/no)
- Recommended statistic to report: mean / **median+IQR**
- Recommended transform: none / log1p(λ=__) / Yeo-Johnson — chosen because: ____
- Valid test family going forward: parametric t-test / non-parametric U / bootstrap CI
- Histogram + QQ plot attached: <plot filename>

## Cross-cutting conclusions
1. Variables where the arithmetic MEAN would mislead stakeholders: ____
2. Variables needing transformation before modeling: ____
3. Hidden segments discovered from multi-modal shapes: ____
