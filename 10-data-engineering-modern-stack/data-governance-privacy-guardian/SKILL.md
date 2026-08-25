---
name: data-governance-privacy-guardian
description: Apply data governance and privacy practice practically — classification, access design, PII minimization, retention, lineage, GDPR/CCPA-ready workflows. Activate when sensitive data flows anywhere or compliance questions arise.
---

# When to use
- Customer/personal data enters analysis environments
- Access is "everyone has admin" chaos
- Audit, DSAR (data subject request), or deletion obligations arrive

# Process
1. **Data inventory & classification** — catalog datasets; tag sensitivity tiers (public / internal / confidential / regulated-PII) with named owners; unknown = treat as highest tier until proven otherwise.
2. **Minimization first** — analysis needs aggregates, not identities: tokenize/hash identifiers, mask direct quasi-identifiers, create de-identified analytical zones as the default working layer.
3. **Access architecture** — role-based least privilege, row/column-level security for shared tables, no shared service accounts for humans, quarterly access reviews.
4. **Retention & deletion** — documented retention per dataset; automated purge jobs; DSAR runbook: locate all data for a subject across systems within the legal window.
5. **Lineage & audit** — transformations logged so any published number traces to source; access logs retained; consent/provenance flags travel with the data.
6. **Pragmatic culture** — governance that blocks work dies; provide fast self-service paths through the compliant route and measure adoption.

# Inputs the skill needs
- Required: systems/data inventory, applicable regulations, existing access model
- Optional: industry-specific rules (HIPAA, PCI), breach history

# Output
- Classification catalog with owners
- De-identified analytics zone + access matrix implementation
- Retention schedule, DSAR runbook, and audit evidence pack

## Execution Protocol

When this skill activates, work in this order:

1. **Read** every file in `references/` listed below BEFORE starting the Process.
2. **Run** the `scripts/` tools on real inputs during the relevant Process steps; capture their console output/plots as evidence.
3. **Deliver** by filling the `assets/` templates - they define the exact output format stakeholders expect.
4. Cite which reference rules guided each judgment call in the final deliverable.

### scripts/ - tools to run
- `scripts/catalog_extractor.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.
- `scripts/pii_scan.py` - Run: python <file> --help, then execute with real inputs; capture output as evidence.

### references/ - knowledge to read
- `references/catalog_standards.md` - maintain as part of the deliverable
- `references/privacy_reference.md` - read before executing the Process

### assets/ - templates to fill and deliver
- `assets/catalog_entry_template.md` - Fill this template - it IS the deliverable format.
- `assets/governance_program_template.md` - Fill this template - it IS the deliverable format.
