# Query Performance Diagnosis Report — <query name>

## 1. Baseline
| Metric | Before |
|---|---|
| Runtime | |
| Rows scanned / bytes scanned | |
| Dominant plan node (the bottleneck) | |
| Spill / shuffle size | |
| Cost (credits) | |

## 2. Root Cause
- Bottleneck node: ____
- Why it happens (plain language): ____
- Anti-patterns found:
  - [ ] SELECT * pulling unneeded columns
  - [ ] non-sargable predicate (function on indexed/partition column)
  - [ ] join before filter / missing partition pruning
  - [ ] distinct/sort causing unnecessary shuffle
  - [ ] joining raw fact table where pre-agg exists

## 3. Rewrite Applied
```sql
-- paste optimized query here
```

## 4. Equivalence Proof
| Check | Original | Rewritten | Match? |
|---|---|---|---|
| row count | | | |
| revenue checksum (sum) | | | |

## 5. Result
| Metric | Before | After | Improvement |
|---|---|---|---|

## 6. Structural Recommendations (if rewrite insufficient)
- Index/clustering key candidate: ____ on columns (____) — expected benefit vs write cost
- Materialized view candidate for repeated aggregation: ____
