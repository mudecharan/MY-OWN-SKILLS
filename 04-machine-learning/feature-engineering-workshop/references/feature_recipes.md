# Feature Engineering Recipe Book

## Datetime alchemy
| Feature | Formula | Why it works |
|---|---|---|
| Cyclical hour/day | sin/cos(2π·value/period) | 23:00 near 00:00 |
| Recency | days since last event (as-of T) | strongest single predictor in most behavioral data |
| Tenure | first event → T | lifecycle stage proxy |
| Velocity ratio | events_30d×3 / events_90d | accelerating vs fading engagement |

## Behavioral aggregates (per entity, window ending at T)
- counts, sums, means per window: 7 / 30 / 90 / all-time
- trend slope over recent windows
- diversity: nunique of categories touched
- gaps between events (mean, max)

## Encoding decision table
| Cardinality | Method |
|---|---|
| ≤ 15 levels | one-hot |
| 15–1000 | frequency/count encoding; or target encoding with out-of-fold + smoothing |
| > 1000 entities | embeddings, or hash trick for streaming |
| Ordinal | explicit ordered mapping — never one-hot |

## Target encoding safety rules
- Compute INSIDE folds only (out-of-fold), never on full training target.
- Smooth toward global mean: `(n·mean_cat + m·global) / (n + m)`, m≈20.
- Keep the category→value map as an artifact for serving.

## Text
TF-IDF (fast baseline) → pretrained sentence embeddings (strong default).

## Validation
1. Permutation importance on held-out data (never train-set importance).
2. Family ablation: drop rolling-windows family → measure delta.
3. Null-importance test: shuffle target, re-rank — real features should stand out.
