# Fraud Analytics Reference

## Fraud typologies to screen first (known patterns)
| Typology | Signature features |
|---|---|
| Card testing | many small amounts, high decline rate, new device |
| Account takeover | login geo/device change + credential reset + quick payout |
| Friendly fraud | legit customer, refund claims post-delivery, repeat pattern |
| Promo abuse | multi-accounting via shared devices/addresses, referral chains |
| Structuring | amounts clustering just under thresholds |
| Bust-out | credit behavior normal → sudden max utilization → vanish |

## Unsupervised discovery discipline
Isolation forest / DBSCAN on behavioral features surfaces NEW typologies —
but clusters need HUMAN labels before acting. Sample 30–50 hits per cluster,
label with analysts, keep only patterns with a coherent story.

## Link analysis is where rings die
Fraudsters look innocent individually. Build an entity graph over shared
devices, addresses, payment instruments, referral edges. Rings = dense components.
Visualize; count entities per component; escalate the top components for review.

## Precision-first doctrine
False positives cost real customers and support load. Tiered responses
(pass / challenge / review / block) let you act at every confidence level
instead of binary blocking. Measure friction cost of challenges too.

## The adversary adapts
Rule effectiveness decays. Monitor hit rates; refresh patterns monthly;
log analyst verdicts as training data. Detection is a maintenance program, not a project.
