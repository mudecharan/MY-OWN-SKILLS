---
name: methodology-explainer
description: Explain HOW an analysis was done to non-technical stakeholders — layered depth, analogies, slide + writeup formats. Activate when trust in the method is questioned or methodology must be presented.
---

# When to use
- Stakeholders ask "how do we know this number is right?"
- A methodology section must accompany a formal report
- Post-decision reviews need reproducibility documentation

# Process
1. Identify the audience depth (see `references/audience_depth_guide.md` — executive /
   manager / technical).
2. Explain in three layers: business question → approach in plain language → data & math
   summary. Use patterns from `references/methodology_explanation_patterns.md`.
3. Fill `assets/methodology_writeup_template.md` for written reports.
4. Fill `assets/methodology_slide_template.md` for presentations.
5. Pre-answer the top 3 challenge questions ("sample size?", "bias?", "why this metric?").

# Inputs the skill needs
- Required: the analysis whose method needs explaining, audience type
- Optional: prior challenges raised about this analysis

# Output
- Methodology write-up section (report-ready)
- Methodology slides (appendix-grade)
- Anticipated-question answers

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/methodology_outline.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/methodology_explanation_patterns.md` - apply these proven patterns

### assets/ - templates to fill and deliver
- `assets/methodology_slide_template.md` - Fill this template - it IS the deliverable format.
- `assets/methodology_writeup_template.md` - Fill this template - it IS the deliverable format.
