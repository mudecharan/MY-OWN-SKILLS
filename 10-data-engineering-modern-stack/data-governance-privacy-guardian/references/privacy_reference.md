# Privacy & Governance Reference

## Sensitivity tiers & default handling
| Tier | Examples | Default rule |
|---|---|---|
| public | published reports | open |
| internal | sales aggregates | employees, RBAC |
| confidential | contracts, salaries | named access only |
| regulated-PII | emails, IDs, health, payment | masked/tokenized everywhere possible; raw locked to process accounts |

## PII minimization in analytics (do this by default)
- Analysis needs AGGREGATES, not identities → build a de-identified zone as the
  default entry point for all analysts.
- Quasi-identifiers re-identify even without names: zip+DOB+gender is unique for
  most people. Generalize (zip3, age bands).
- Hashed emails are STILL personal data under GDPR — tokenization limits exposure,
  it doesn't remove obligation.

## DSAR basics
GDPR: respond within one month. Two request types: access ("what do you hold")
and erasure ("delete it"). You need a reliable subject-search across systems —
build that index BEFORE the first request arrives.

## Retention discipline
Every dataset gets a retention rule at creation time; purge jobs automated;
"we might need it someday" is not a retention policy.

## Pragmatism principle
Governance that blocks work gets bypassed and dies. Provide FAST self-service
through the compliant route and measure adoption of the de-identified zone.
