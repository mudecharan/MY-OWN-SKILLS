# Funnel Optimization Reference

## Definition decisions (make them explicit or numbers are meaningless)
- Ordered vs unordered funnel: did step N+1 BEFORE step N count?
- Window: same session? 7 days? Lifetime? Choose by decision cycle.
- Re-entry: returning users who repeat steps — first occurrence is standard.

## Priority math (the part everyone skips)
Don't fix the worst % drop; fix the biggest OPPORTUNITY:
`opportunity = dropped users × downstream value at stake`
A 5% leak before purchase beats a 40% leak after it.

## Time-to-convert as a friction detector
Raw drop-off hides stalls. A median of 3 days between signup and activation
means users churn INSIDE the gap — session replays and error logs tell you why.

## Simpson's paradox discipline
Always break steps by device, source, new/returning. Aggregate "improvements"
sometimes mask a segment regressing — and that segment finds out publicly.

## Guardrails for conversion tests
Conversion rate up but downstream quality down = losing. Always pair:
signup rate ↔ activated rate · purchase rate ↔ refund rate · speed ↔ completion.
