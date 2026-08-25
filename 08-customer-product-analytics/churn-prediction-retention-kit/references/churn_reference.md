# Churn & Retention Reference

## Defining churn correctly (per business model)
| Model | Churn definition | Trap |
|---|---|---|
| Contractual SaaS | cancellation at renewal | involuntary churn (payment failure) mixed in — split it |
| Non-contract e-commerce | no purchase in N days | N from return-rate curve: pick where P(return after t) < 5% |
| Marketplace | inactivity per side | supply churn hides demand churn |

## Prediction horizon discipline
If retention actions need 60 days of lead time, predicting churn 7 days before
renewal is operationally useless regardless of AUC. Horizon = lead time + margin.

## Features that usually carry signal
Usage decline VELOCITY (not level) · support contact escalation pattern · billing failures
· feature breadth shrinkage · champion-user departure (B2B) · tenure × plan interactions

## Save-value matrix logic
Intervention ROI = P(churn) × save_rate × customer_value − cost.
The sweet spot is high-risk × savable × valuable. Low-value high-risk → cheap automation or let go.
Save rate MUST be measured against a randomized holdout — "saved" customers often
were never leaving.

## Operational loop
Weekly scored list → CS plays → outcomes logged → model retrained quarterly.
A churn model without an intervention loop is a very expensive dashboard.
