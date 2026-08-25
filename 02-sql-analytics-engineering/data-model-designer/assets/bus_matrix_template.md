# Bus Matrix — <business process inventory>

Fill: rows = fact tables (processes), columns = conformed dimensions. ✓ = dimension applies.

| Fact table | Grain | date | customer | product | store | employee | campaign |
|---|---|---|---|---|---|---|---|
| fact_orders (order line) | | ✓ | ✓ | ✓ | ✓ | | ✓ |
| fact_returns (return line) | | ✓ | ✓ | ✓ | ✓ | | |
| fact_sessions (session) | | ✓ | ✓ | ✓ | | | |
| fact_support_tickets (ticket) | | ✓ | ✓ | | | ✓ | |

## SCD assignments
| Dimension | Attribute | SCD type | Rationale |
|---|---|---|---|
| customer | region | Type 2 | historical reporting by old regions required |
| customer | email correction | Type 1 | error fix, no history needed |
| product | list price | Type 2 | margin must reflect price at sale time |

## Measure additivity check
| Measure | Additive over | Note |
|---|---|---|
| line_revenue | date, customer, product | fully additive |
| account_balance | nothing | semi-additive: sum over customers OK, NOT over dates → snapshot grain |
| discount_% | nothing | non-additive: recompute from numerator/denominator |
