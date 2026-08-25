# Credit Risk Model Package — <score name>

## 1. Definitions
| Item | Definition |
|---|---|
| Default event | |
| Observation date / outcome window | |
| Exclusions + rationale | |

## 2. Population & stability
Development sample: n=____ , default rate ____
PSI dev→current applicant pool: ____ (<0.1 required)

## 3. Model
| Item | Value |
|---|---|
| Technique (scorecard / GBM+calibration) | |
| Features (availability-checked at decision time ☐) | |
| Out-of-time AUC ± CI | |
| Calibration table (predicted vs realized PD by decile) | attached |

## 4. Operating recommendation
| PD cut-off | Approval rate | Bad rate (approved) | Expected loss | Profit/applicant |
|---|---|---|---|---|
Recommended cut-off with finance sign-off: ____

## 5. Governance artifacts
- [ ] reason-code mapping for declines (top 3 drivers each)
- [ ] monitoring plan: PSI monthly, AUC quarterly on maturing vintages
- [ ] annual validation scheduled; owner: ____
