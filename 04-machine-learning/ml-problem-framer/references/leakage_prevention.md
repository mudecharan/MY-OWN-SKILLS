# Leakage Prevention Reference

## The golden timeline rule
For a prediction made at time T, every feature must exist strictly before T.
Draw the timeline for EVERY feature; if you can't date it, treat it as leaked.

## Classic leakage vectors
| Vector | Example | Defense |
|---|---|---|
| Post-outcome fields | "days_since_last_login" computed at dataset end, not prediction time | recompute as-of T |
| Aggregates over the full period | customer lifetime total including post-churn activity | rolling windows ending at T |
| Target proxies | "cancellation_reason" for churn prediction | drop fields filled only after Y |
| Group leakage | same customer in train AND test | GroupShuffleSplit / time split |
| Preprocessing leakage | scaler/imputer fit on full data | Pipeline fit on train only |

## Split selection
| Data shape | Correct split |
|---|---|
| Time-ordered anything | TimeSeriesSplit / hold out latest period |
| Repeated entities | GroupKFold on entity id |
| Independent rows | StratifiedKFold |

## Smell test
If your model's most important feature is one a business person says
"wait, that's only known after the fact" — you have leakage. AUC of 0.99 on
tabular business data is a bug until proven otherwise.
