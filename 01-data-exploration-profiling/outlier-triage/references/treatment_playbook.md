# Outlier Classification & Treatment Playbook

## Classification (assign EVERY flagged point one of three labels)
| Label | Definition | Correct action |
|---|---|---|
| **Data error** | Impossible or provably wrong (negative price, unit error, duplicate with typo) | Trace to source; correct if evidence exists; else exclude with rule |
| **Legitimate extreme** | Real but rare (whale customer, Black Friday spike) | KEEP; switch to robust statistics (median, trimmed mean, quantile regression) |
| **Out-of-scope population** | Belongs to a different analysis (B2B orders inside B2C extract) | Exclude with documented filter; route to its own analysis |

## Treatment options ranked by preference
1. **Fix at source** — always best when the error is provable.
2. **Keep + robust stats** — median/MAD, trimmed means, Huber loss, quantile regression.
3. **Winsorize/cap** — at P1/P99 or business bound; report both raw and capped figures.
4. **Transform** — log1p for right-skewed monetary values (handles the tail naturally).
5. **Exclude** — LAST resort; only with a written, reusable rule + audit log.

## Never do
- Silent deletion.
- One-off manual row drops in a notebook that will be re-run.
- Treating a seasonal spike as an outlier (check the calendar first).

## Sensitivity rule of thumb
If removing flagged points shifts a headline metric by >5%, the report MUST show both views.
