---
name: dataset-first-look
description: Rapid structured first-pass profiling of any unfamiliar dataset. Activate the moment a new file, table, or extract lands — before any business question is answered.
---

# When to use
- A new CSV/Parquet/Excel/database table arrives with no documentation
- You inherit someone else's dataset and need a trust-but-verify pass
- Starting any analysis; this skill produces the "Section 0" of every report

# Process
1. **Identity** — row count, column count, memory footprint, dtypes. Confirm grain: what does ONE row represent? State it in plain words.
2. **Keys & uniqueness** — identify natural keys, check duplicates at the declared grain, flag surrogate-key gaps.
3. **Null map** — per-column null % and null pattern (random vs blocks → hints at upstream failures).
4. **Cardinality scan** — high-cardinality (IDs), low-cardinality (flags/dimensions), constants (dead columns).
5. **Temporal envelope** — min/max dates, gaps in time coverage, timezone sanity.
6. **Value sanity** — negatives where positives expected, impossible values (age 250), mixed types in text columns.
7. **Verdict card** — 1-page summary: usable as-is / usable-with-caveats / blocked, plus top 5 issues.

# Inputs the skill needs
- Required: path to dataset or connection details
- Optional: claimed grain from the data owner (to validate against)

# Output
- Filled `assets/profile_report.md`: identity block, null heatmap data, cardinality table
- Verdict card with go/no-go for downstream analysis

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/data_overview.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/duplicate_finder.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/freshness_check.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/null_counter.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/null_profiler.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/profile_dataset.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/eda_checklist.md` - work through item-by-item during the Process; confirm each box
- `references/pandas_polars_recipes.md` - use these proven patterns when implementing
- `references/profiling_checklist.md` - work through item-by-item during the Process; confirm each box
- `references/quality_dimensions.md` - read before starting.

### assets/ - templates to fill and deliver
- `assets/audit_report_template.html` - Styled output format - generate/populate and deliver.
- `assets/eda_report_template.md` - Fill this template - it IS the deliverable format.
- `assets/findings_summary.md` - Fill this template - it IS the deliverable format.
- `assets/profile_report_template.md` - Fill this template - it IS the deliverable format.
- `assets/quality_rubric.md` - Fill this template - it IS the deliverable format.
