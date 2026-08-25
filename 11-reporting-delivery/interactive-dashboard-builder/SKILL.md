---
name: interactive-dashboard-builder
description: Build self-serve interactive HTML dashboards (Plotly) that stakeholders explore themselves — filters, drill-downs, hover details — as a single shareable file. Activate when users need to explore, not just read.
---

# When to use
- Stakeholders keep asking follow-up questions a static report can't answer
- A lightweight interactive view is needed without BI-server infrastructure
- Exploratory analysis results must be browsable by non-analysts

# Process
1. Confirm the primary exploration questions and required filters (see
   `references/interactivity_patterns.md`).
2. Prepare an aggregate dataset per visual (dashboards must NOT query raw facts).
3. Run `scripts/build_interactive_dashboard.py --config dashboard_config.json`
   to generate a single self-contained `dashboard.html` (Plotly + dropdown filters).
4. Open the file and run the 5-second test: primary question answerable immediately?
5. Verify performance (<5s load), then hand over with usage guidance.

# Inputs the skill needs
- Required: aggregate datasets (CSV/parquet), key questions, filter dimensions
- Optional: brand colors, refresh cadence

# Output
- Self-contained `dashboard.html` (works offline, shareable via email/drive)
- Data-refresh note: which tables, how often, owner

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/build_interactive_dashboard.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/interactivity_patterns.md` - apply these proven patterns

### assets/ - templates to fill and deliver
- `assets/dashboard_spec_template.md` - Fill this template - it IS the deliverable format.
