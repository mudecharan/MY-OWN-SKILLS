---
name: executive-narrative-writer
description: Turn analysis into executive-ready narratives — pyramid principle, answer-first structure, one-message-per-slide, action-oriented recommendations. Activate when findings go upward to decision-makers.
---

# When to use
- Presenting analysis to leadership/board
- Written summaries accompanying deep-dive reports
- Any communication where attention is scarce and stakes high

# Process
1. **Governing thought** — one sentence containing the recommendation + its strongest justification; if you can't write it, the analysis isn't done.
2. **Pyramid build** — answer at top → 3 supporting arguments (MECE) → evidence under each; cut everything not load-bearing for the recommendation.
3. **Slide discipline** — each slide: action title (the takeaway, not the topic), one message, one visual max; body text only when unavoidable.
4. **Anticipate the room** — pre-write answers to the 3 hardest questions (usually methodology trust, cost, risk); put backups in appendix.
5. **Quantify the ask** — every narrative ends with: decision needed, by whom, by when, resources required, and what happens next week if approved.
6. **Edit ruthlessly** — read aloud test; kill hedges ("might possibly"), jargon, and methodology talk unless challenged.

# Inputs the skill needed
- Required: completed analysis findings, decision context, audience seniority
- Optional: time slot length, prior related decisions

# Output
- Executive summary document / slide deck outline
- Governing-thought statement + supporting argument map
- Anticipated-Q&A appendix

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/jargon_detector.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/narrative_linter.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/readability_scorer.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/audience_depth_guide.md` - read before executing the Process
- `references/communication_rules.md` - apply these rules; they override defaults
- `references/data_writing_guide.md` - read before executing the Process
- `references/executive_communication.md` - read before starting.
- `references/insight_framework.md` - structure your work with this framework
- `references/metaphor_bank.md` - read before starting.
- `references/narrative_frameworks.md` - structure your work with this framework
- `references/prioritization_guide.md` - read before executing the Process
- `references/pyramid_principle_guide.md` - read before executing the Process
- `references/stakeholder_personas.md` - read before starting.
- `references/translation_pattern_library.md` - read before starting.

### assets/ - templates to fill and deliver
- `assets/analysis_doc_template.md` - Fill this template - it IS the deliverable format.
- `assets/executive_summary_template.md` - Fill this template - it IS the deliverable format.
- `assets/insight_brief_template.md` - Fill this template - it IS the deliverable format.
- `assets/narrative_template.md` - Fill this template - it IS the deliverable format.
- `assets/narrative_worksheet.md` - Fill this template - it IS the deliverable format.
- `assets/translation_template.md` - Fill this template - it IS the deliverable format.
