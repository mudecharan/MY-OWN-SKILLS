# MLOps for Small Teams (no Kubernetes required)

## Packaging minimum bar
- Pinned environment: `requirements.txt` with exact versions OR container image digest.
- Artifact versioning: model file + training-data hash + git SHA in one metadata JSON.
- Preprocessing lives in the same code path as training (sklearn Pipeline / saved transformer).
  Two implementations of "the features" = guaranteed silent drift.

## Deployment ladder (cheapest first)
| Stage | What | When |
|---|---|---|
| Batch scoring | cron job writes scores to warehouse table | most business problems; start here |
| Shadow service | real-time endpoint logging predictions, unused | before replacing a decision |
| Progressive live | % traffic or champion/challenger | after shadow passes |

## Monitoring without a platform
- Scheduled job computes PSI per feature vs stored reference → writes to `model_monitor` table.
- BI alert on that table. This is 90% of commercial drift tooling.

## Retraining discipline
Retraining is a RELEASE: same eval gates, human approval, rollback path.
Automated retraining without gates just automates shipping regressions.

## Incident class you WILL hit
Upstream team changes a column's meaning silently → scores go garbage.
Defense: schema contract checks + PSI alerts catch it within a day instead of a quarter.
