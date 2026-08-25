---
name: significance-explainer
description: Translate statistical testing correctly for decision-makers and catch common misuse — p-value myths, confidence-interval meaning, multiple comparisons, practical vs statistical significance. Activate when results must be interpreted or defended.
---

# When to use
- Someone reads "p = 0.06" as "no effect" or "p < 0.001" as "huge effect"
- A review challenges your methodology
- Choosing whether a finding justifies action

# Process
1. **Separate the two questions** — Is there evidence of an effect? (statistics) vs Is the effect big enough to matter? (business). Answer both, explicitly.
2. **Effect size first** — lead with the estimate and CI in real units ("+1.8pp conversion [95% CI: −0.2 to +3.8]"), never the p-value alone.
3. **Myth sweep on every reported number** — p ≠ P(hypothesis true); non-significant ≠ proven equal; CI overlap ≠ no difference; n grows → trivial effects become "significant".
4. **Multiplicity audit** — count all comparisons made (metrics × segments × periods); apply Holm/Benjamini-Hochberg where family-wise or discovery control matters; disclose the count honestly.
5. **Robustness trio** — re-check under alternative tests (parametric/non-parametric), outlier treatments, and subgroup definitions; fragile findings get labeled fragile.
6. **Verdict language** — map evidence strength to recommended action: strong → ship; moderate → pilot; weak/null → don't conclude equality, state what sample size WOULD answer it.

# Inputs the skill needs
- Required: the statistical output being interpreted (test, estimate, CI, p)
- Optional: how many comparisons were explored, the decision context

# Output
- Correct interpretation paragraph ready for the report
- Myth-correction notes where misuse occurred
- Multiplicity-adjusted results table and action recommendation

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/assumptions_tracker.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/multiplicity_audit.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/evidence_rules.md` - apply these rules; they override defaults
- `references/hypothesis_testing_guide.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/assumptions_log_template.md` - Fill this template - it IS the deliverable format.
- `assets/interpretation_card_template.md` - Fill this template - it IS the deliverable format.
