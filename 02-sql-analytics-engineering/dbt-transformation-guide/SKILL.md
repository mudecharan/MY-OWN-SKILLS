---
name: dbt-transformation-guide
description: Structure warehouse transformations as a tested dbt project — staging/intermediate/marts layers, tests, docs, exposures. Activate when ad-hoc SQL must become a governed, versioned transformation codebase.
---

# When to use
- The same logic lives in five dashboards and they disagree
- Onboarding analysts requires tribal knowledge about table meanings
- You want CI-tested, documented transformations

# Process
1. **Project scaffold** — folder layout (`staging/`, `intermediate/`, `marts/`), naming conventions (`stg_<source>__<entity>`), source definitions in YAML pointing at raw tables.
2. **Staging layer** — 1:1 light transforms only: renames, type casts, timezone normalization; no business logic here.
3. **Marts layer** — dimensional models per the business process; reusable macros for repeated logic (date spines, UTM parsing); generic tests (unique, not_null, accepted_values, relationships) plus singular tests encoding business rules.
4. **Refactor safely** — migrate legacy SQL model-by-model; prove parity with side-by-side output comparison before cutting over.
5. **Docs & lineage** — descriptions on every model and column that a stakeholder would ask about; generate and review the DAG for cycles/density smells.
6. **CI hook** — `dbt build --select state:modified+` slim-CI pattern on PRs.

# Inputs the skill needs
- Required: warehouse connection, raw source inventory, priority models to build first
- Optional: existing dbt project to refactor, style guide

# Output
- Working dbt project structure with sources, models, tests, docs
- Parity evidence for any migrated logic
- Lineage graph + generated documentation site content

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/dbt_scaffold.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/metric_template_generator.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/model_yaml_validator.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/dbt_conventions.md` - read before starting.
- `references/dbt_semantic_layer_guide.md` - read before executing the Process
- `references/metric_definition_framework.md` - structure your work with this framework

### assets/ - templates to fill and deliver
- `assets/fct_model_example.sql` - Adapt and run; paste results into the report template.
- `assets/metric_definition.yaml` - Complete as the deliverable.
- `assets/schema_tests.yml` - Adapt into your project configuration.
