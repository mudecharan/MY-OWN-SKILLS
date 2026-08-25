# Model Evaluation Report — <model>

## Split integrity verdict
- [ ] Time-based split (if temporal) — holdout period: ____
- [ ] Group-aware split (entities don't cross train/test)
- [ ] Feature availability timeline audited — no post-T fields
- Verdict: PASS / FAIL (details: ____)

## Headline metrics with bootstrap CIs (n=1000 resamples)
| Metric | Value | 95% CI |
|---|---|---|
| | | |

## Calibration
| Decile | predicted | actual | n |
|---|---|---|---|
Verdict: calibrated / needs Platt / needs isotonic

## Threshold economics
Cost matrix used: FP=__ FN=__ TP value=__
Optimal operating point: threshold ____ → net value ____ (vs default 0.5: ____)

## Slice table
| Segment | n | Metric | Flag (<90% of overall?) |
|---|---|---|---|

## Model comparison (if applicable)
| Model | Metric ± CI | Complexity cost | Winner |
|---|---|---|---|

## Recommendation
Deploy at threshold ____ · monitor slices ____ · recheck after ____
