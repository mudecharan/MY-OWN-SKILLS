# Imputation Decision Tree

```
Column has missing values
│
├─ Missing % < 5 AND mechanism MCAR?
│   └── YES → listwise deletion acceptable (document row loss)
│
├─ Time series column?
│   ├── gap length <= 2-3 periods → interpolation / forward-fill WITHIN entity only
│   └── gap spans structural break → do NOT fill; flag period
│
├─ Mechanism = MAR (missingness explained by other observed columns)?
│   ├── Modeling use case → MICE / KNN / missForest; fit on TRAIN only;
│   │                     add was_missing indicator if missingness is informative
│   └── Descriptive stats → multiple imputation (m=5+), pool results (Rubin's rules)
│
├─ Mechanism = MNAR (missingness depends on the unobserved value itself,
│   e.g. high earners hide income)?
│   └── Imputation WILL bias results. Options:
│       1) analyze observed-only with explicit caveats
│       2) sensitivity analysis under range of assumptions
│       3) escalate: better data collection is the real fix
│
└─ Categorical column?
    → mode imputation hides signal; prefer "Missing" as explicit category
      (missingness itself often predicts outcomes)
```

## Hard rules
- Never compute imputation parameters using test-set rows.
- Never impute the TARGET variable for supervised learning — drop those rows.
- Every imputed dataset ships with a "what was filled and how" appendix table.
