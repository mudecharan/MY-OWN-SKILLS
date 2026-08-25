---
name: customer-segmentation-builder
description: Create actionable customer segments via RFM and unsupervised clustering — with segment naming, profiling, stability testing, and activation mapping. Activate when marketing/CRM needs "treat different customers differently."
---

# When to use
- One-size-fits-all campaigns underperform
- CRM/personalization strategy needs a customer typology
- Resource allocation across accounts (who gets the human touch?)

# Process
1. **Segmentation purpose first** — what decisions will segments drive? (media targeting, retention offers, sales tiers). Purpose dictates features.
2. **RFM foundation** — Recency, Frequency, Monetary computed on clean transaction data; check distributions before scoring; use quintiles, not arbitrary cutoffs.
3. **Model-based extension** — k-means/GMM on standardized behavioral + attitudinal features (if survey data exists); choose k by silhouette + business interpretability, not elbow alone; validate cluster stability across bootstrap samples.
4. **Profile & name** — each segment gets a vivid name ("Dorming Big Spenders"), size, value share, defining behaviors, and an evidence table — never Cluster 1–5.
5. **Actionability audit** — can we actually reach/target each segment with available channels? Merge unactionable fragments.
6. **Activation kit** — per segment: recommended plays, expected value shift, owner, and measurement plan (segment KPIs tracked quarterly for drift).

# Inputs the skill needs
- Required: transactional history per customer, contactability data
- Optional: survey/attitudinal data, product usage events

# Output
- Segment model with validated k and stability evidence
- Segment profile book (names, sizes, behaviors, value)
- Activation playbook linking each segment to concrete actions

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/segment_builder.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/segmentation_runner.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/segmentation_approaches.md` - read before starting.
- `references/segmentation_playbook.md` - follow these rules when classifying/deciding

### assets/ - templates to fill and deliver
- `assets/segment_book_template.md` - Fill this template - it IS the deliverable format.
- `assets/segment_profile_template.md` - Fill this template - it IS the deliverable format.
