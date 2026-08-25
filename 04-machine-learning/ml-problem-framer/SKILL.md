---
name: ml-problem-framer
description: Convert a vague business wish into a well-posed ML problem — target definition, unit of prediction, label construction, feasibility triage, success criteria. Activate BEFORE any modeling starts.
---

# When to use
- Someone says "we should use AI/ML on this" with no concrete target
- A modeling project stalls because nobody agrees what it predicts
- Deciding whether ML is even the right tool vs rules or analytics

# Process
1. **Decision-first framing** — identify the decision the prediction enables, who acts on it, and when; a model that doesn't change an action has no value.
2. **Target engineering** — define Y precisely and at what timestamp ("churned = no purchase in 90 days after subscription expiry"); check target availability and quality in data.
3. **Unit & horizon** — one row = which entity at which time? Prediction horizon must exceed action lead time (predicting churn 2 days before renewal is useless if retention needs 60 days).
4. **Feasibility triage** — signal audit (do similar features correlate with Y historically?), class balance, label latency, volume; score against "rules could do this" alternative.
5. **Success criteria** — minimum metric uplift vs current process to justify deployment, measured in business value (e.g., "catch 30% more churners at same contact budget").
6. **Anti-leakage contract** — list features by their availability timestamp; anything post-prediction-time is banned.
7. **Scope document** — problem statement, unit/horizon/target, constraints, MVP plan.

# Inputs the skill needs
- Required: business goal, available data inventory, the operational decision
- Optional: current manual-process performance as baseline

# Output
- One-page ML problem specification (target, unit, horizon, success bar)
- Feasibility verdict with go/no-go recommendation
- Feature-availability timeline preventing leakage

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/feasibility_probe.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/leakage_prevention.md` - read before starting.

### assets/ - templates to fill and deliver
- `assets/problem_spec_template.md` - Fill this template - it IS the deliverable format.
