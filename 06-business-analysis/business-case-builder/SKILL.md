---
name: business-case-builder
description: Construct a decision-grade business case — options, costs, quantified benefits with ranges, NPV/ROI/payback, risks, and a clear recommendation. Activate when an initiative needs funding approval.
---

# When to use
- Proposing a project/tool/hire that requires budget approval
- Comparing build-vs-buy or vendor options
- Challenging someone else's business case with rigor

# Process
1. **Decision framing** — the choice being made, who decides, deadline, and what happens if nothing is done (do-nothing baseline is mandatory).
2. **Option generation** — ≥3 real options including do-nothing and do-minimum; each described in one crisp paragraph.
3. **Cost modeling** — one-time (build, implementation) vs recurring (licenses, ops, maintenance); include hidden costs: migration, training, parallel-run, internal time.
4. **Benefit quantification** — every benefit as formula × driver ("support tickets 12k/mo × 15% deflection × $8/ticket"); use ranges (conservative/expected/optimistic), never single points; label hard savings vs soft/strategic.
5. **Financial appraisal** — NPV at company discount rate, IRR if useful, payback period, sensitivity table on the two biggest assumptions.
6. **Risk register** — top 5 risks with likelihood×impact and mitigations; state the kill criteria (when to abort).
7. **Recommendation** — one option, one paragraph why, first 90 days plan.

# Inputs the skill needs
- Required: initiative description, cost inputs available, decision context
- Optional: company discount rate, comparable past projects

# Output
- Complete business case document (options → financials → risks → recommendation)
- Sensitivity analysis showing which assumptions matter most
- One-page executive version

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/confidence_interval.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/cost_savings.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/financials.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/revenue_impact.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/assumption_documentation.md` - read before starting.
- `references/business_case_rules.md` - apply these rules; they override defaults
- `references/impact_quantification_framework.md` - structure your work with this framework
- `references/risks_dependencies.md` - read before starting.

### assets/ - templates to fill and deliver
- `assets/business_case_template.md` - Fill this template - it IS the deliverable format.
- `assets/business_case_template_src.md` - Fill this template - it IS the deliverable format.
- `assets/impact_estimate_template.md` - Fill this template - it IS the deliverable format.
