---
name: dashboard-wireframer
description: Design dashboards people actually use — audience-driven layout, the 5-second question test, performance-conscious chart choices, and a maintenance plan. Activate before building any dashboard in any BI tool.
---

# When to use
- A dashboard request arrives (most die from over-building)
- An existing dashboard is ignored or slow
- Migrating reports into Power BI/Tableau/Looker

# Process
1. **Audience & job** — who opens it, when, to decide what? One primary question per dashboard; everything else is secondary. If there's no recurring decision, recommend a report instead.
2. **Wireframe first** — sketch layout BEFORE touching the BI tool: top-left = headline KPIs with vs-target deltas; middle = drivers; detail tables last (or linked out). Apply F-pattern reading.
3. **Interaction design** — minimal cross-filtering that serves real questions; date-range default = business cycle; no 12 dropdowns nobody uses.
4. **Performance engineering** — aggregate tables under visuals, avoid live direct queries on facts, limit high-cardinality visuals; page load target <5s or usage will die.
5. **Trust features** — every tile shows refresh timestamp + source; documented metric definitions linked on-page.
6. **Launch & prune** — usage monitoring after 30 days; remove unused tiles (they add maintenance cost); schedule quarterly review.

# Inputs the skill needs
- Required: audience, decisions supported, data sources available
- Optional: BI tool constraints, existing dashboards to consolidate

# Output
- Wireframe/layout spec ready to build
- Metric definition list per visual with source mapping
- Performance and maintenance checklist

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/perf_budget.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/dashboard_design_principles.md` - apply these principles throughout
- `references/dashboard_requirements_guide.md` - read before executing the Process
- `references/dashboard_rules.md` - apply these rules; they override defaults

### assets/ - templates to fill and deliver
- `assets/dashboard_spec_template.md` - Fill this template - it IS the deliverable format.
- `assets/wireframe_spec_template.md` - Fill this template - it IS the deliverable format.
