# Credit Scoring Reference

## Target & window definitions (write them down first)
- Default event: e.g., 90+ days past due, charge-off, or bankruptcy within outcome window
- Observation point → outcome window must match business cycle (12 months typical)
- Exclude: loans too young to have matured (censoring!), fraud-confirmed cases (separate model)

## Population honesty
You can only model APPROVED applicants — rejects never got the chance to default.
This is reject inference bias. Consequences: score degrades as you expand approvals.
Mitigations: monitor PSI between development population and current applicants;
champion/challenger on thin-file segments.

## Scorecard vs ML trade-offs
| | Classic scorecard (WOE + logistic) | GBM + calibration |
|---|---|---|
| Interpretability/regulator comfort | ★★★ | needs SHAP layer |
| Performance | good | usually better |
| Reason codes | native | mapped from SHAP |

## Calibration is not optional
Decisions use PD × LGD × EAD. A model that only RANKS cannot price risk.
Calibrate with isotonic/Platt on out-of-time data; check mean-predicted ≈ realized.

## Cut-off selection
Plot approval rate vs expected loss AND profit per applicant. The operating point
is a business decision with finance at the table. Report: approval rate,
bad-rate among approved, expected loss, profit.

## Ongoing governance
PSI monthly · AUC on maturing vintages quarterly · annual full validation ·
adverse-action reason codes for every decline.
