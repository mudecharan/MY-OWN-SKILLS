# Segmentation Playbook Reference

## Purpose before features
| Decision segments must drive | Feature emphasis |
|---|---|
| Media targeting | demographics + channel behavior |
| Retention offers | recency/frequency trends, support contacts |
| Sales tiering (who gets human touch) | account value + growth potential |
| Product roadmap | usage patterns by feature depth |

## RFM scoring rules
- Quintiles computed on rank(method='first') to break ties deterministically.
- Recency inverted: FEWER days = better = score 5.
- RFM cells (555, 111...) map to classic plays: champions / loyal / at-risk / hibernating.
- RFM alone is a fine v1 — ship it in a week, upgrade to clustering later.

## Clustering hygiene
- Log-transform monetary & frequency (heavy skew) BEFORE standardizing.
- Choose k by silhouette AND business interpretability; 4–7 usable segments typical.
- Stability: split-half ARI or bootstrap re-fit agreement >0.6, else k is noise-fitting.
- NEVER name clusters "Cluster 1..5" — profile each and give vivid names.

## Actionability audit
| Check | If it fails |
|---|---|
| Can we target this segment via available channels? | merge into neighbor segment |
| Does the segment differ on an ACTIONABLE dimension? | re-cluster with different features |
| Is the segment stable quarter over quarter? | features too noisy |

## Activation kit per segment
Name · size · value share · defining behaviors · recommended play · owner · KPI to watch.
