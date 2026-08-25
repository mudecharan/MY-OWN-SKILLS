---
name: master-qa-checklist
description: Run the full quality-assurance pass over any analysis before it ships — accuracy, logic, communication, reproducibility — plus peer review and retrospective. Activate before ANY deliverable leaves your hands.
---

# When to use
- Mandatory gate before every report, dashboard, or model ships
- Peer-reviewing a colleague's analysis
- Closing out a project with a retrospective

# Process
1. Work through `references/qa_checklist_master.md` — data, logic, statistics, communication sections.
2. Cross-check against `references/common_analysis_errors.md` (the classic blunders list).
3. Run `scripts/qa_runner.py --report <findings.md>` for automated checks (numbers cited
   vs computed, TODO markers, hedge-word scan).
4. For peer review: apply `references/peer_review_framework.md` and
   `references/code_review_for_analysis.md`; fill `assets/peer_review_template.md`;
   the author responds via `assets/review_response_template.md`.
5. Verify `references/analytical_rigor_checklist.md` items for statistical claims.
6. Collect sign-off in `assets/qa_signoff_template.md`.
7. After delivery, run the retro: `assets/retrospective_template.md` +
   `references/retro_frameworks.md`; log lessons in `assets/learnings_log_template.md`.

# Inputs the skill needs
- Required: the draft deliverable + its underlying analysis
- Optional: reviewer names, project context

# Output
- Completed QA checklist with pass/fail per item
- Peer review document + author responses
- Signed QA sign-off; retrospective + learnings log entry

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/qa_runner.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/analytical_rigor_checklist.md` - work through item-by-item during the Process; confirm each box
- `references/code_review_for_analysis.md` - read before starting.
- `references/common_analysis_errors.md` - read before starting.
- `references/learning_capture.md` - read before starting.
- `references/peer_review_framework.md` - structure your work with this framework
- `references/qa_checklist_master.md` - work through item-by-item during the Process; confirm each box
- `references/retro_frameworks.md` - structure your work with this framework

### assets/ - templates to fill and deliver
- `assets/learnings_log_template.md` - Fill this template - it IS the deliverable format.
- `assets/peer_review_template.md` - Fill this template - it IS the deliverable format.
- `assets/qa_signoff_template.md` - Fill this template - it IS the deliverable format.
- `assets/retrospective_template.md` - Fill this template - it IS the deliverable format.
- `assets/review_response_template.md` - Fill this template - it IS the deliverable format.
