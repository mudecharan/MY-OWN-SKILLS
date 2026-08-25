---
name: market-swot-competitor-analyst
description: Data-driven market and competitor analysis — SWOT grounded in evidence, competitor benchmarking, market sizing (TAM/SAM/SOM), positioning gaps. Activate for strategy work needing numbers behind the narrative.
---

# When to use
- Strategy/planning cycles requiring competitive intelligence
- Market entry or product launch assessments
- Replacing opinion-based SWOTs with evidence-based ones

# Process
1. **Market sizing** — TAM (top-down from industry data), SAM (filter by segment/geography fit), SOM (bottom-up from your funnel capacity); show both methods where possible and reconcile.
2. **Competitor matrix** — pick 5–8 competitors; compare on measurable dimensions: pricing, feature coverage, traffic/audience estimates, hiring signals, review scores, release cadence.
3. **Evidence gathering** — public filings, job postings (what they're building), app-store changelogs, pricing pages (archive history), community sentiment mining; cite every claim.
4. **Evidence-based SWOT** — each S/W/O/T item requires ≥1 data point; convert vague items ("strong brand") into proxies (share-of-search, NPS benchmarks).
5. **Positioning gap analysis** — plot the market on 2 axes that matter to buyers (from review mining, not assumption); identify white space vs crowded zones honestly.
6. **Strategic options** — derive 3 moves from the analysis, each with supporting evidence and a validation experiment.

# Inputs the skill needs
- Required: company context, competitor list, market segment definition
- Optional: internal win/loss data, subscription budget for data providers

# Output
- Market sizing memo with TAM/SAM/SOM reconciliation
- Competitor benchmarking matrix with cited evidence
- SWOT + positioning map + three validated strategic options

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/market_sizing.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/competitive_intel_methods.md` - read before starting.

### assets/ - templates to fill and deliver
- `assets/market_analysis_template.md` - Fill this template - it IS the deliverable format.
