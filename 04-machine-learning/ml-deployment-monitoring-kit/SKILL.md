---
name: ml-deployment-monitoring-kit
description: Take a validated model to production safely — packaging, shadow deployment, rollback, drift monitoring, retraining triggers. Activate when a model moves from notebook to serving real decisions.
---

# When to use
- A model passed evaluation and must start scoring real traffic
- A deployed model silently degraded and nobody noticed for months
- Setting up MLOps practices for a small team without heavy infrastructure

# Process
1. **Package for reproducibility** — pinned environment (lockfile/container), versioned artifacts with training-data hash, config-driven preprocessing (same code path as training).
2. **Shadow mode first** — serve predictions alongside existing process WITHOUT acting on them; compare agreement and outcomes for 2–4 weeks.
3. **Progressive rollout** — 5%→25%→100% traffic or champion/challenger split; define automatic rollback triggers (error rate, score distribution shift).
4. **Monitoring triad**:
   - Data drift: PSI/KS per feature vs training reference (>0.25 PSI = investigate)
   - Prediction drift: score distribution shifts
   - Performance: delayed-label metrics once ground truth matures
5. **Retraining policy** — trigger = drift breach OR calendar OR performance floor; retrain uses fresh window, passes same evaluation gates as v1; never auto-promote.
6. **Runbook** — ownership, alert routing, kill switch procedure, last-known-good artifact.

# Inputs the skill needs
- Required: trained model artifact, serving environment options, label-return delay
- Optional: existing orchestration/registry tooling

# Output
- Deployed service in shadow mode with rollout plan
- Monitoring dashboard spec + alert thresholds
- Retraining policy doc and incident runbook

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/psi_monitor.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/mlops_small_team.md` - read before starting.

### assets/ - templates to fill and deliver
- `assets/monitoring_spec_template.md` - Fill this template - it IS the deliverable format.
