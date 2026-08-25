---
name: funnel-optimizer
description: Analyze and optimize conversion funnels — step-level drop-off, segment comparison, statistical validation of improvements, experiment backlog. Activate for signup, checkout, onboarding, or any multi-step flow.
---

# When to use
- Users abandon somewhere between landing and purchase
- Checkout/onboarding redesign needs baseline and targets
- "Where should we focus optimization effort?" needs an answer

# Process
1. **Funnel definition** — explicit steps with event definitions; decide handling of out-of-order events and re-entries; state the session/user window.
2. **Step economics** — drop-off rate AND exit-value per step; rank steps by lost-opportunity volume (drop-offs × downstream value), not just worst percentage.
3. **Segment decomposition** — break each step by device, source, new/returning; Simpson's paradox check — aggregate improvements sometimes hide segment regressions.
4. **Time-to-convert** — distribution of inter-step durations; long stalls reveal friction points invisible in raw drop-off.
5. **Hypothesis backlog** — per priority step: candidate causes (from session replays, error logs, field analytics), proposed fix, expected lift estimate, test design.
6. **Validation loop** — A/B test top fixes with power analysis; track guardrails (downstream quality of converted users, not just conversion rate).

# Inputs the skill needs
- Required: event data covering all funnel steps
- Optional: session recordings/tools, error telemetry

# Output
- Funnel baseline report with prioritized opportunity ranking
- Segment breakdown exposing paradox risks
- Ranked experiment backlog with expected-lift estimates

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/funnel_analysis.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/funnel_analyzer.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/funnel_design_guide.md` - read before executing the Process
- `references/funnel_reference.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/funnel_backlog_template.md` - Fill this template - it IS the deliverable format.
- `assets/funnel_report_template.md` - Fill this template - it IS the deliverable format.
