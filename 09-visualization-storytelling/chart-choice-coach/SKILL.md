---
name: chart-choice-coach
description: Pick the correct visualization for every data-and-message combination and execute it cleanly — encodings, axis discipline, color semantics, annotation. Activate before any chart leaves your hands.
---

# When to use
- Building any report or slide containing charts
- A chart feels "off" but you can't say why
- Reviewing others' visualizations

# Process
1. **Message-first** — state the takeaway in one sentence ("Churn doubled in EMEA"); the sentence picks the chart, not the data type alone.
2. **Relationship routing**:
   - Comparison → bars (sorted!); part-to-whole → stacked/100% (pie only if ≤3 slices); trend → line; distribution → histogram/box/violin; correlation → scatter; flow → Sankey
   - Never: dual-axis line charts of different units without extreme care; 3D anything; truncated bar axes
3. **Encoding discipline** — position > length > angle > color for accuracy; zero-baseline bars; consistent color = consistent meaning across all charts in the deliverable.
4. **Declutter pass** — remove gridline excess, redundant legends, borders; max ~4 colors; direct-label series instead of legend-hunting.
5. **Annotate the insight** — highlight the one point that matters; add the "so what" as a title/subtitle, not buried in an appendix.
6. **Accessibility check** — colorblind-safe palettes (viridis/Okabe-Ito), contrast ratios, readable at print size.

# Inputs the skill needs
- Required: dataset/chart to improve or create, audience context
- Optional: brand style guide constraints

# Output
- Corrected/new charts with message-driven titles
- Before/after rationale notes (teaches the team)
- Reusable style settings (palette, fonts) for consistency

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/chart_builder_src.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/chart_builders.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/chart_matrix.md` - use to route decisions
- `references/chart_selection_guide.md` - read before executing the Process
- `references/visual_design_principles.md` - apply these principles throughout

### assets/ - templates to fill and deliver
- `assets/style_settings.md` - Fill this template - it IS the deliverable format.
- `assets/viz_spec_template.md` - Fill this template - it IS the deliverable format.
