# Data Governance & Privacy Program — <org>

## 1. Classification catalog
| Dataset | Sensitivity tier | Owner (person) | Location | Notes |
|---|---|---|---|---|
Tiers: public / internal / confidential / regulated-PII
Rule: unclassified = treat as highest tier until proven otherwise.

## 2. De-identified analytics zone (default working layer)
| Technique | Applied to | Notes |
|---|---|---|
| tokenized/hashed IDs | user_id, email | salt stored separately |
| masked quasi-identifiers | zip→zip3, DOB→age band | re-identification risk reduced |
| aggregate-only views | everything PII-adjacent | k-anonymity threshold __ |

## 3. Access architecture
| Principle | Implementation |
|---|---|
| least privilege RBAC | role matrix below |
| row/column-level security on shared tables | policy: ____ |
| no shared human service accounts | |
| quarterly access review, owner: ____ | last review date: ____ |

## 4. Retention & deletion
| Dataset class | Retention | Purge mechanism | Automated? |
|---|---|---|---|

## 5. DSAR (data subject request) runbook summary
1. Receive request → log with deadline (30d GDPR)
2. Locate all data for subject across systems (search keys: ____)
3. Fulfill access/erasure per legal basis
4. Confirm completion + evidence retained

## 6. Lineage & audit
Published numbers traceable to source: ☐ · access logs retained ____ · consent flags travel with data ☐

## Culture metric
Time-to-compliant-access for a new analyst: target <1 day — governance that blocks work dies.
