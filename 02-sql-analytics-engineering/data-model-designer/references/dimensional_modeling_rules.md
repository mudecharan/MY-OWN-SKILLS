# Dimensional Modeling Design Rules

## Process
1. One fact table per business process — never "one big table for everything".
2. Grain sentence BEFORE columns: "One row = one order line at time of purchase."
   Every column must be true at that grain; anything else goes to a dimension.
3. Facts are numbers you ADD (or snapshot); descriptive text belongs in dimensions.

## SCD decision table
| Change example | Type | Handling |
|---|---|---|
| Typo correction | 1 | overwrite |
| Region/segment/price change worth history | 2 | new row: valid_from/valid_to/is_current |
| "Current view only" attribute | 3 | extra prior-value column (rare) |
| Never changes (birth date) | 0 | freeze |

## Fact table flavors
- **Transaction** — event grain, sparse, biggest
- **Periodic snapshot** — one row per entity per period (balances, inventory)
- **Accumulating snapshot** — one row per workflow, milestone dates updated

## Keys
- Surrogate keys everywhere in facts/dims (never join on business keys directly)
- Late-arriving dimensions → insert "Unknown" member with key -1, backfill later

## Design smells
- Fact table without a date key ❌
- Dimensions with 1:1 rows to facts (should be degenerate dims) ⚠️
- Multi-valued attributes crammed into a dimension column (→ bridge table) ⚠️

## Validation gate
Run the top 5 stakeholder questions against the prototype model.
If any needs >4 joins or a window function hack, the model is wrong.
