# Capacity Planning Formulas Reference

## Core staffing equation (long-interval approximation)
```
Required FTE = (Forecast Volume × AHT) / (Available minutes × (1 − Shrinkage) × Occupancy_target)

AHT        = average handle time incl. after-call wrap-up
Shrinkage  = breaks + training + meetings + absence (typ. 25–35%)
Occupancy  = share of logged-in time actually handling work (target 75–85%)
```

## Interval-level support staffing → Erlang C
For service-level targets ("80% answered within 20s"), the FTE formula is not enough:
use Erlang C (traffic intensity A = λ × AHT in Erlangs; agents N such that
P(wait > t) = C(N,A)·exp(−(N−A)·t/AHT) ≤ 1 − SL).
Libraries: `erlang-c` pip package, or `pyworkforce.queuing.ErlangC`.

## Utilization guardrail
Above ~85% occupancy queues grow non-linearly (M/M/N math) and burnout spikes.
Planning at 100% = guaranteed SLA collapse.

## Scenario grid (always build)
| Demand | Attrition low | Attrition high |
|---|---|---|
| Base | | |
| +20% | | |
| −20% | | |

Hiring lead time (recruit+train ≈ 8–12 weeks) must precede each capacity break date.

## Efficiency levers (quantify each in FTE-equivalents)
| Lever | Typical effect |
|---|---|
| Self-service deflection | 10–30% volume reduction |
| AHT reduction (tooling/knowledge) | 5–15% |
| Schedule optimization / shift alignment | 5–10% effective capacity |
