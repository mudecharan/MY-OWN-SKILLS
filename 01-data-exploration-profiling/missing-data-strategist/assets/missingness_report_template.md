# Missing Data Treatment Report — <dataset>

## 1. Missingness Summary
| Column | Missing % | Pattern (random/block/time-bound) | Co-missing with |
|---|---|---|---|

## 2. Mechanism Verdict
| Column | Verdict (MCAR/MAR/MNAR) | Evidence | Confidence |
|---|---|---|---|

*Evidence examples: group-mean shifts on missing-vs-present, block patterns by date/system, domain knowledge about capture process.*

## 3. Treatment Applied
| Column | Method chosen | Parameters | Why (link to decision tree branch) |
|---|---|---|---|
| | median / MICE / KNN / forward-fill / category="Missing" / deletion | | |

## 4. Recovery Validation (10% artificial masking)
| Column | Method | MAE | Compare-to baseline (median-only) |
|---|---|---|---|

## 5. Uncertainty Impact
- Headline estimate without treatment: __
- With multiple imputation (m=5): __ ± __
- Conclusion changed by imputation choice? Yes / No

## 6. Caveats for Final Report
-
