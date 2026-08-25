# Causal Analysis Report — <question>

## 1. Question & DAG
- Causal claim under test: "<T> causes <Y> by <amount>"
- DAG (list edges): T → Y; Z1 → T; Z1 → Y; ...
- Backdoor paths to block: ____
- Colliders identified (DO NOT adjust): ____

## 2. Method(s) applied & assumption audit
| Method | Key assumption | Could it fail here? | Sensitivity check run | Result |
|---|---|---|---|---|
| DiD | parallel trends | | pre-trend event study | |
| PSM | ignorability | | Rosenbaum bounds / balance table | |

## 3. Estimates
| Method | Effect | 95% CI | Business interpretation |
|---|---|---|---|

## 4. Triangulation verdict
- Methods agree / disagree because: ____
- Final claim with confidence boundary:
  "We estimate <effect>; we are confident the direction is __; magnitude could plausibly range __–__ because ____."

## 5. What would change our mind
-
