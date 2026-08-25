---
name: process-mapper-analyst
description: Map and quantify business processes from event data — as-is flows, bottleneck detection via timestamps, rework loops, automation candidates. Activate when operations feel slow but nobody can say where they leak.
---

# When to use
- Order-to-cash, hiring, claims, ticket workflows take too long
- Preparing for automation/RPA — need evidence of what to automate
- Post-reorg process redesign

# Process
1. **Event extraction** — pull timestamped activity logs (case ID, activity, timestamp, actor); validate case completeness and clock sanity.
2. **As-is discovery** — reconstruct actual flow variants (not the documented ideal); rank variants by frequency; the "top 5 variants cover X% of cases" insight usually shocks stakeholders.
3. **Bottleneck quantification** — waiting time vs working time per step; longest-wait league table; identify steps where 80% of elapsed time accumulates.
4. **Rework & loop detection** — repeated activities per case (approvals bounced back), SLA breach rates per stage, handover count correlation with duration.
5. **Conformance check** — compare observed flow against the official process; document deviations and their cost.
6. **Improvement shortlist** — score each candidate fix by time-saved × frequency ÷ effort; flag automation candidates (rule-based, high-volume, low-judgment steps) separately from elimination/redesign candidates.

# Inputs the skill needs
- Required: event/activity log data with timestamps, process understanding from an owner
- Optional: SLA definitions, cost-per-hour figures

# Output
- As-is process maps (real variants, with frequencies)
- Bottleneck report: waiting-time league table
- Ranked improvement backlog with estimated impact

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/process_discovery.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/process_mining_reference.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/findings_template.md` - Fill this template - it IS the deliverable format.
