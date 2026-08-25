# Business Case Quality Rules

## The do-nothing baseline is mandatory
Every benefit is measured AGAINST what happens without the project.
"Save 2 FTE of manual work" means nothing unless you show the work growing,
the error rate, and the cost of status quo.

## Benefit formulas, never adjectives
Bad: "significant efficiency gains."
Good: "12k tickets/mo × 15% deflection × $8/ticket = $14.4k/mo."

## Ranges beat points
Present conservative / expected / optimistic. If the case only survives
under optimistic assumptions, say so out loud.

## Hidden costs checklist
migration · parallel-run period · training & adoption curve · internal staff time
· ongoing maintenance (rule of thumb: 15–25% of build cost per year) ·
license true-ups · decommissioning the old thing.

## Sensitivity analysis
Vary the TWO biggest drivers ±50%; if NPV flips negative in any plausible cell,
state it as a condition ("case holds if deflection ≥10%").

## Kill criteria are a feature
Pre-agreed abort conditions make approvers braver — a case without them reads as overconfidence.

## Financial quick reference
- NPV = Σ CF_t / (1+r)^t − initial; reject if <0 vs alternatives
- Payback = when cumulative CF crosses zero
- Soft benefits allowed but labeled soft and capped at ~30% of claimed value
