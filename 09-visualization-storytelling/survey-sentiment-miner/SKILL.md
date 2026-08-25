---
name: survey-sentiment-miner
description: Extract signal from unstructured feedback — NPS/CSAT verbatims, reviews, support tickets — via theme mining, sentiment scoring, driver correlation, and trend tracking. Activate when customer voice exists as free text.
---

# When to use
- Thousands of survey comments nobody reads
- NPS dropped and the "why" lives in verbatims
- Product teams need evidence-backed theme priorities

# Process
1. **Corpus preparation** — dedupe, filter spam/bot text, language handling, PII scrubbing before any processing.
2. **Theme extraction** — start unsupervised (embedding clustering / keyword co-occurrence) to discover themes; then refine into a stable codebook (~10–20 named themes) applied consistently over time.
3. **Sentiment with care** — transformer-based classifiers beat lexicons on sarcasm/negation; validate against 200 hand-labeled samples; report accuracy honestly; theme × sentiment matrix.
4. **Driver linkage** — join themes back to structured scores (NPS, CSAT, churn): which themes correlate with detractors or cancellations? Quantify: "shipping-delay mentions = 31% of detractor comments".
5. **Trend & alerting** — monthly theme-volume tracking; alert on emerging themes (>3σ volume jump) — new problems announce themselves in text first.
6. **Closing the loop** — deliver ranked themes to owning teams with verbatim evidence packs; track whether mentioned issues actually improve.

# Inputs the skill needs
- Required: free-text feedback + any accompanying scores/metadata
- Optional: product area taxonomy for mapping themes

# Output
- Theme codebook + sentiment model with validated accuracy
- Theme×sentiment×score driver analysis
- Monthly trend dashboard spec and evidence packs per team

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/feedback_miner.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/mining_reference.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/voc_report_template.md` - Fill this template - it IS the deliverable format.
