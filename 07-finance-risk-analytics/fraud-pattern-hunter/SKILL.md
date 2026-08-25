---
name: fraud-pattern-hunter
description: Hunt fraud and abuse patterns in transactional data — rule mining, unsupervised anomaly detection, network/link analysis, precision-first alert design. Activate when losses, chargebacks, or abuse patterns need investigation.
---

# When to use
- Chargeback/refund rates climbing without explanation
- Promo/bonus abuse suspected
- Designing detection before losses compound

# Process
1. **Loss quantification** — measure exposure by channel, geography, payment method, time; establish the baseline so impact is provable.
2. **Known-pattern screening** — velocity rules (N cards per device/hour), mismatch signals (IP-billing country), structuring amounts (just-under thresholds), duplicate fingerprints.
3. **Unsupervised discovery** — isolation forest / DBSCAN on behavior features to surface NEW patterns not covered by known typologies; human-label a sample of hits.
4. **Link analysis** — build entity graphs (shared devices, addresses, payment instruments, referral chains) to expose organized rings that look innocent individually.
5. **Precision-first deployment** — false positives cost real customers; tune for precision at workable recall; tiered response (challenge/hold/review/block) instead of binary block.
6. **Adversarial loop** — fraud adapts; monitor rule hit-rate decay, schedule monthly pattern refresh, log analyst feedback.

# Inputs the skill needs
- Required: transaction/event data with device/network metadata, loss labels where available
- Optional: confirmed fraud cases for supervised evaluation

# Output
- Quantified loss/exposure report by dimension
- Discovered pattern catalog with evidence
- Deployable rule/detection set with expected precision and alert volumes

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/fraud_scan.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/fraud_reference.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/pattern_catalog_template.md` - Fill this template - it IS the deliverable format.
