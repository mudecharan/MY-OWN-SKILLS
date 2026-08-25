---
name: feature-engineering-workshop
description: Systematically transform raw columns into predictive features — datetime decomposition, aggregation windows, encoding strategy, text/embedding basics — with leakage-safe pipelines. Activate during model development when raw fields underperform.
---

# When to use
- Model performance plateaus despite algorithm tuning
- Rich raw logs (timestamps, text, transactions) sit unused
- Building a reusable feature pipeline for production

# Process
1. **Domain mining session** — brainstorm features WITH a domain expert; ask "what would you check manually to predict this?" Those answers are the best features.
2. **Datetime alchemy** — decompose to cyclical encodings (sin/cos hour-of-day, day-of-week), recency gaps, "days since last event", holiday/proximity flags.
3. **Behavioral aggregates** — rolling windows (7/30/90-day counts, sums, trends, velocity ratios like spend-this-week-vs-trailing-average); align windows strictly before the prediction timestamp.
4. **Encoding decisions** — one-hot (<15 levels), frequency/count encoding, target encoding ONLY with out-of-fold computation + smoothing, embeddings for high-cardinality entities.
5. **Text & interactions** — TF-IDF/embedding features where relevant; interaction terms guided by domain logic, not brute force.
6. **Pipeline hygiene** — build all transforms inside sklearn Pipeline/ColumnTransformer so train/test separation is structural; validate via permutation importance and ablation (drop feature group → measure delta).

# Inputs the skill needs
- Required: training dataset, target, prediction-time boundary
- Optional: entity-level event history (enables rich aggregates), expert access

# Output
- Feature engineering module (importable, tested)
- Feature importance/ablation report showing each family's contribution
- Feature dictionary documenting every derived column's formula and window

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/feature_builder.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/feature_recipes.md` - use these proven patterns when implementing

### assets/ - templates to fill and deliver
- `assets/feature_dictionary_template.md` - Fill this template - it IS the deliverable format.
