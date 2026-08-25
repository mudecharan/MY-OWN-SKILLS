# Feature Dictionary — <model>

All windows computed as-of prediction timestamp T. Nothing after T may appear.

| Feature | Formula / Source | Window | Type | Owner | Notes |
|---|---|---|---|---|---|
| recency_days | min(days_before_snapshot) | as-of T | numeric | | |
| n_events_30d | count(events) | 30d ending T | numeric | | |
| velocity_ratio | n_30d×3 / n_90d | 30/90d | numeric | NaN→median at serve | |
| last_hr_sin/cos | sin/cos(2π·hour/24) of last event | as-of T | numeric | | cyclical |
| <cat>_freq | category frequency in train | train stats | numeric | refresh quarterly | |

## Family ablation results (held-out metric delta)
| Family removed | Metric change | Verdict keep/drop |
|---|---|---|

## Serving notes
- Computed where (warehouse/dbt/online service): ____
- Refresh cadence & staleness tolerance: ____
