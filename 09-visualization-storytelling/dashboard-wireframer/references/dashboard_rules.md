# Dashboard Design Rules

## Why most dashboards die
No recurring decision behind them. The intake question is:
"Who opens this, when, to decide WHAT?" If there's no answer, build a report
(one-time narrative) instead of a dashboard (living tool).

## The 5-second test
A stranger should answer the dashboard's primary question within 5 seconds.
Headline KPIs with vs-target deltas at top-left; detail below the fold.

## Layout physics
- F-pattern reading: top-left is prime real estate.
- 3–5 headline KPIs maximum; more = none of them matter.
- Detail tables last or linked out — nobody opens a dashboard to scroll a 10k-row table.

## Performance engineering (usage dies above 5s load)
- Aggregate/pre-aggregate tables under visuals; BI tools should never scan raw facts.
- Limit high-cardinality visuals (scatter with 1M points, 200-slice pies).
- Materialize the dashboard's source model; incremental refresh where possible.

## Trust features
Refresh timestamp + source on every tile · metric definitions one click away ·
consistent color semantics across pages.

## Maintenance reality
30-day usage review → prune dead tiles. Every tile is a permanent maintenance
liability; dashboards only survive with scheduled gardening.
