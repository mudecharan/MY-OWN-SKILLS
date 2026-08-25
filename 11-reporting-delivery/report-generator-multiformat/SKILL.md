---
name: report-generator-multiformat
description: Generate stakeholder-ready analysis reports in Markdown, styled HTML, and PDF from one content source. Activate when findings must be delivered as a polished written report.
---

# When to use
- Any completed analysis needs a written deliverable
- The same report must go out in multiple formats (email body, web link, PDF attachment)
- Recurring reports (weekly/monthly) need consistent structure

# Process
1. Gather the analysis outputs (tables, metrics, charts) and confirm the audience & decision.
2. Read `references/report_design_standards.md` and `references/context_layering_guide.md`.
3. Write the report content into `assets/report_template.md` structure:
   answer first, key numbers, evidence, caveats, next steps.
4. Run `scripts/generate_report.py --input report.md --formats html,pdf` to produce
   the styled HTML and print-ready PDF versions.
5. Check length budget with `scripts/token_counter.py`; tighten before sending.
6. Run the master QA checklist (`11-reporting-delivery/master-qa-checklist`) before delivery.

# Inputs the skill needs
- Required: analysis findings, audience, delivery format(s)
- Optional: brand style constraints, charts/images to embed

# Output
- `report.md`, `report.html`, `report.pdf` — same content, three formats
- Delivery note listing assumptions and data freshness

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/context_bundler.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/generate_report.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/token_counter.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/context_layering_guide.md` - read before executing the Process
- `references/context_quality_rubric.md` - read before starting.
- `references/report_design_standards.md` - meet these standards in the deliverable

### assets/ - templates to fill and deliver
- `assets/context_package_template.md` - Fill this template - it IS the deliverable format.
- `assets/report_template.md` - Fill this template - it IS the deliverable format.
