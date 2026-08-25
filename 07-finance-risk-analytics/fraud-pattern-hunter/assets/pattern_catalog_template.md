# Fraud Pattern Catalog — <portfolio>

## 1. Loss quantification (the baseline everything is measured against)
| Dimension | Loss $ | Chargeback % | Trend |
|---|---|---|---|
| by channel | | | |
| by geography | | | |
| by payment method | | | |
| by time (day/hour pattern) | | | |

## 2. Known-pattern screening rules deployed
| Rule | Logic | Hit rate | Precision (confirmed fraud / hit) |
|---|---|---|---|
| velocity | >N cards per device/24h | | |
| geo mismatch | IP country ≠ billing country | | |
| structuring | amounts just under threshold ($90–99) | | |

## 3. Newly discovered patterns (unsupervised)
| Cluster ID | Distinguishing features | Human-labeled verdict | Action |
|---|---|---|---|

## 4. Link analysis findings
Shared attributes across "unrelated" accounts:
| Attribute (device/address/payment instrument) | Entities sharing it | Ring hypothesis |
|---|---|---|

## 5. Tiered response design
| Risk band | Response | Expected false-positive cost |
|---|---|---|
| low | pass | — |
| medium | challenge (3DS / step-up) | friction only |
| high | hold + review | reviewer capacity |
| extreme | block | rare; strong evidence required |

## 6. Adversarial maintenance
Rule hit-rate decay monitored: ☐ · pattern refresh cadence: monthly · analyst feedback loop: ____
