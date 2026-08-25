---
name: market-basket-affinity-analyzer
description: Mine product co-purchase patterns — association rules, affinity lift, complement/substitute detection, cross-sell recommendation design. Activate for merchandising, bundling, and recommendation use cases.
---

# When to use
- Cross-sell/email recommendations are guesswork
- Store layout or site merchandising decisions
- Bundle design needs evidence

# Process
1. **Basket construction** — define basket grain (order/session/visit-window); filter noise (staff accounts, bulk buyers) that distort rules.
2. **Association mining** — Apriori/FP-Growth for frequent itemsets; rank rules by support × confidence × LIFT; discard lift ≤1 immediately (no real affinity).
3. **Interpretation layer** — classify top pairs: complements (buy together), substitutes (rarely together but same category), seasonal co-occurrence artifacts (sunscreen + ice cream in July — don't bundle-pricing-decide on those).
4. **Segment-aware affinities** — mine within key segments; affinities differ (new vs returning, region, channel).
5. **Application mapping** — translate rules to placements: "frequently-bought-together" carousels, checkout add-ons, email cross-sell, bundle candidates with pricing math (bundle must beat sum-of-parts margins).
6. **Measure** — A/B the placement changes; track attach rate and incremental margin, not just clicks.

# Inputs the skill needs
- Required: transaction-level order lines (order ID, product, qty)
- Optional: product hierarchy, campaign calendar

# Output
- Affinity rule table (filtered for lift >1, interpretable)
- Complement/substitute classification of key pairs
- Placement/bundle recommendations with expected-margin logic

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/basket_affinity.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/basket_reference.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/affinity_findings_template.md` - Fill this template - it IS the deliverable format.
