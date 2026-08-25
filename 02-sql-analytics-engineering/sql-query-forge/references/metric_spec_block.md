# Metric Specification Block (fill BEFORE writing any SQL)

## Question → Spec
| Item | Value |
|---|---|
| Business question (verbatim from stakeholder) | |
| Metric definition (formula) | |
| Output grain ("one row per ___") | |
| Time window + timezone + boundary rule | |
| Inclusions / exclusions (tests, refunds, internal accounts) | |
| Dimensional breakdowns required | |
| Reconciliation target ("must match finance's X within 0.5%") | |

## Edge-case checklist (tick before delivery)
- [ ] NULL join keys handled (explicit LEFT JOIN + coalesce, or excluded on purpose?)
- [ ] Fan-out checked: joining orders→items multiplies revenue? pre-aggregate first
- [ ] Zero-division guarded with NULLIF
- [ ] Half-open date ranges (`>= start AND < end`) — no double counting at boundaries
- [ ] Late-arriving records: is "as-of today" vs "as-of period close" decided?
- [ ] Duplicates removed via ROW_NUMBER/QUALIFY with deterministic ordering
- [ ] Type-2 dimension joins use date-range predicate (valid_from <= t < valid_to)
- [ ] Row counts verified at each CTE stage

## Assumptions embedded as SQL comments
Every judgment call becomes a comment line next to the code that implements it.
