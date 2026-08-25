# Requirements Elicitation Playbook

## The core insight
The stated ask is rarely the real need. "Send me a weekly report of orders" usually means
"I get blamed when stockouts happen and I need early warning." Interview until you reach
the decision; then design for the decision.

## Question sequences that work
| Situation | Ask |
|---|---|
| Vague ask | "Walk me through the last time you made this decision. What did you look at?" |
| Feature request | "If this number doubles tomorrow, what would you do?" (if answer is 'nothing', it's a vanity metric) |
| Report refresh request | "Show me your current spreadsheet" — reverse-engineer it as the draft spec |
| Deadline pressure | "What decision slips if this arrives a week later?" — recalibrates urgency honestly |

## Testable requirement format
Every line must be verifiable:
> "For region R and month M, show SUM(net_revenue) where status IN ('paid','shipped'),
> currency converted to USD at month-end rate, sorted descending."

Not: "show sales by region."

## MoSCoW discipline
Must-haves only in phase 1. Every Could is written down and DEFERRED IN WRITING —
this single habit prevents 80% of scope creep.

## Change management
Post-sign-off changes go through a logged trade-off: "adding X costs Y days or drops Z."
Never absorb silently.
