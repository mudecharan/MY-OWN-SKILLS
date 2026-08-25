# KPI Design Rules

## Metric tree logic
North-star outcome metrics move slowly and can't be acted on directly.
Driver KPIs are the levers; diagnostics explain WHY a driver moved.
If you can't draw the causality arrow upward, the metric doesn't belong in the tree.

## Definition rigor checklist
- [ ] Formula unambiguous (numerator, denominator, time basis)
- [ ] Grain stated (per user? per order? per week?)
- [ ] Named human owner — teams don't own metrics, people do
- [ ] Exclusions documented ("excludes wholesale", "excludes trials")
- [ ] Single source query/table referenced

## Target setting from strategy math
Work backward: "To hit $50M ARR at 110% NRR, need $X expansion + $Y new logos/mo,
which implies Z qualified leads/week at current conversion." Targets derived this way
survive scrutiny; round numbers picked in offsites don't.

## Anti-gaming pre-mortem (do it for every efficiency metric)
Ask: "How would a smart, incentivized person hit this number while hurting the business?"
Then add the counterweight metric that catches exactly that behavior.
Classic pairs: speed↔quality · volume↔accuracy · growth↔retention · cost↔CSAT.

## Cadence discipline
Metrics reviewed nowhere get deleted. Dashboards nobody opens get archived.
Fewer, owned, acted-upon metrics beat comprehensive dashboards every time.
