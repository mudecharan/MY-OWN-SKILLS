---
name: data-model-designer
description: Design dimensional and analytical data models — star schemas, SCD handling, grain decisions, surrogate keys, bus matrix. Activate when building a warehouse model or fixing a tangled join mess.
---

# When to use
- Analysts write 8-way joins to answer simple questions
- A new business process needs a home in the warehouse
- Slowly-changing attributes (price changes, re-orgs) corrupt historical reporting

# Process
1. **Business process selection** — pick ONE process (orders, sessions, claims); list its business questions to anchor design.
2. **Grain declaration** — state the atomic grain of the fact table in one sentence; every design decision defers to it.
3. **Dimensions** — identify conformed dimensions; define attributes stakeholders filter/group by; assign SCD strategy per attribute (Type 1 correct-errors, Type 2 preserve history, Type 0 immutable).
4. **Facts** — additive vs semi-additive vs non-additive measures (balances need snapshot grains!); degenerate dimensions for transaction IDs.
5. **Bus matrix** — rows = facts, columns = dimensions; mark coverage; expose gaps as future work.
6. **Keys & integrity** — surrogate key generation rules, late-arriving dimension handling ("unknown" members).
7. **Validation** — prototype DDL + sample load; run the top-5 business questions against it and measure query simplicity.

# Inputs the skill needs
- Required: business process description, source tables/fields available
- Optional: history-retention requirements, BI tool conventions

# Output
- Model spec: fact/dimension tables with grain statements and SCD assignments
- Bus matrix diagram (markdown table)
- DDL + seed script demonstrating the model end-to-end

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/referential_integrity.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/schema_compare.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/validate_model.sql` - Run against your warehouse (adapt dialect); capture results as evidence.

### references/ - knowledge to read
- `references/dimension_hierarchy_patterns.md` - apply these proven patterns
- `references/dimensional_modeling_rules.md` - apply these rules; they override defaults
- `references/schema_mapping_patterns.md` - apply these proven patterns

### assets/ - templates to fill and deliver
- `assets/bus_matrix_template.md` - Fill this template - it IS the deliverable format.
- `assets/dimension_definition.yaml` - Complete as the deliverable.
- `assets/entity_definition.yaml` - Complete as the deliverable.
- `assets/schema_mapping_template.md` - Fill this template - it IS the deliverable format.
- `assets/star_schema_ddl.sql` - Adapt and run; paste results into the report template.
