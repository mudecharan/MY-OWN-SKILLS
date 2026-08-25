---
name: requirements-elicitation-pro
description: Extract complete, testable analytics/data requirements from stakeholders through structured questioning — turning vague asks into signed-off specs. Activate when a stakeholder says "I need a report/dashboard/analysis" without specifics.
---

# When to use
- Intake of any new analytics request
- Requirements documents for BI builds or data products
- Uncovering the real question behind a stated request

# Process
1. **Five-layers-deep probe** — asked want → underlying decision → action they'd take → frequency/urgency → success definition. ("What would you DO differently based on this number?")
2. **Context inventory** — current workaround (the spreadsheet is always the spec), consumers and their data literacy, environment where output lands.
3. **Specification grid** — dimensions × measures × filters × grain × time behavior; write each as testable statement: "For region R and month M, show sum(X) where Y, sorted by Z."
4. **Edge-case interrogation** — new/missing segments, partial months, returns/cancellations, timezone boundaries, permission visibility per role.
5. **Prioritize** — MoSCoW split; explicitly defer nice-to-haves to phase 2 in writing.
6. **Sign-off artifact** — one-page spec + mock-up sketch; no build starts without written agreement; changes after sign-off go through a change log.

# Inputs the skill needs
- Required: access to the requesting stakeholder (30–45 min)
- Optional: existing reports being replaced, sample of their manual work

# Output
- Signed-off requirement specification with edge cases
- Mock-up/wireframe of the deliverable
- Change log establishing scope discipline

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/spec_generator.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/decision_maker_framework.md` - structure your work with this framework
- `references/effort_estimation.md` - read before starting.
- `references/elicitation_playbook.md` - follow these rules when classifying/deciding
- `references/elicitation_techniques.md` - read before starting.
- `references/scoping_framework.md` - structure your work with this framework

### assets/ - templates to fill and deliver
- `assets/analysis_brief_template.md` - Fill this template - it IS the deliverable format.
- `assets/analysis_plan_template.md` - Fill this template - it IS the deliverable format.
- `assets/interview_guide.md` - Fill this template - it IS the deliverable format.
- `assets/kickoff_doc_template.md` - Fill this template - it IS the deliverable format.
- `assets/requirements_doc_template.md` - Fill this template - it IS the deliverable format.
- `assets/requirements_spec_template.md` - Fill this template - it IS the deliverable format.
