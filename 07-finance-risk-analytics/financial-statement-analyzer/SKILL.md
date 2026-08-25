---
name: financial-statement-analyzer
description: Deep analysis of financial statements — ratio frameworks (DuPont), trend and common-size analysis, cash-flow quality checks, red-flag detection. Activate for evaluating company health, due diligence, or benchmarking.
---

# When to use
- Assessing a company/partner/vendor's financial health
- Preparing internal performance reviews against industry benchmarks
- Due diligence support with structured evidence

# Process
1. **Normalize first** — common-size statements (every line as % of revenue / total assets); 3–5 year trends; adjust one-offs flagged in footnotes.
2. **Ratio framework** — DuPont decomposition of ROE (margin × turnover × leverage); liquidity (current, quick), solvency (debt/EBITDA, interest coverage), efficiency (DSO, DIO, DPO → cash conversion cycle), growth quality.
3. **Cash-flow truth test** — reconcile net income vs operating cash flow over time; persistent divergence flags accrual-heavy earnings; FCF conversion ratio trend.
4. **Red-flag scan** — receivables growing faster than revenue, inventory spikes, declining gross margin with rising revenue, capitalized-cost shifts, auditor changes, related-party notes.
5. **Benchmark** — compare ratios vs industry medians (or closest public comparables); flag outliers in both directions.
6. **Synthesis** — one-page credit-style assessment: strengths, concerns, watch items, overall trajectory verdict.

# Inputs the skill needs
- Required: 3+ years of financial statements (or access to them)
- Optional: industry benchmarks, footnote disclosures

# Output
- Common-size + ratio tables across periods
- Red-flag report with evidence citations
- Executive assessment memo with trajectory verdict

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/ratios.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/ratio_redflag_reference.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/financial_report_template.md` - Fill this template - it IS the deliverable format.
