# KPI Framework — <org/team>

## Metric tree (strategy → drivers → diagnostics)
```
North-star outcome: <e.g., Net Revenue Retention>
├── Driver KPI: <e.g., logo retention>          owner: ____
│   ├── Diagnostic: churn reasons mix           owner: ____
│   └── Diagnostic: at-risk account coverage    owner: ____
├── Driver KPI: <e.g., expansion revenue>       owner: ____
│   ├── Diagnostic: usage growth per account
│   └── Diagnostic: upsell pipeline conversion
```
Rule: every branch answers "what causes movement in the parent?"

## Definition catalog (one row per KPI)
| KPI | Exact formula | Grain | Source table | Refresh | Owner (person) | Exclusions |
|---|---|---|---|---|---|---|

## Targets
| KPI | Baseline (from history) | Committed target | Stretch | Basis of target math |
|---|---|---|---|---|

## Anti-gaming guardrails
| Efficiency metric | Paired quality counterweight | Gaming scenario pre-mortem |
|---|---|---|
| tickets closed/agent | CSAT + reopen rate | closing without resolution → reopen tracked |

## Review cadence
| Forum | Frequency | Metrics reviewed | Decisions expected |
|---|---|---|---|

## Sunset list
Metrics not acted on for 2 cycles → removed (with date): ____
