# Churn Program Design — <product>

## Definitions locked with business
| Item | Definition | Agreed by |
|---|---|---|
| Churn event | | |
| Prediction horizon (= action lead time + margin) | | |
| Voluntary vs involuntary split | |

## Model results
AUC ____ · decile table attached

| Decile | Churn rate | Lift × |
|---|---|---|

## Drivers by segment
| Segment | Top drivers | Actionable? (Y/N) | Play triggered |
|---|---|---|---|

## Save-value matrix
| Risk band | Customers | Expected annual save $/cust | Intervention cost | Net | Play |
|---|---|---|---|---|---|

## Plays library
| Driver pattern | Play | Owner | A/B test design |
|---|---|---|---|
| usage declining | onboarding check-in call | CS lead | 50/50 holdout |
| price-driven | plan-fit review | sales | geo split |

## Operating cadence
Weekly risk list delivery: day/time ____, recipients ____
Save-rate measurement: always vs randomized holdout ☐ · model decay review quarterly ☐
