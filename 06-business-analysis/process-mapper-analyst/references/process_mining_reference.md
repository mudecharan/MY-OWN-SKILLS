# Process Mining Quick Reference

## Data requirements (IEEE XES in spirit)
- case_id — one process instance
- activity — named step, consistent vocabulary
- timestamp — complete, correct timezone; sort ties deliberately
- optional: resource, cost, attributes for slicing

Data prep is 70% of the work: dedupe retransmitted events, handle clock skew,
decide whether parallel activities get artificial ordering.

## Core analyses
1. **Variant discovery** — real flows vs documented flow. "Top 5 variants cover X%"
   is usually the most surprising number in the report.
2. **Waiting vs working time** — waiting dominates knowledge-work processes;
   measure handover waits between activities, not just activity durations.
3. **Rework loops** — same activity >1× per case signals upstream quality failure.
4. **SLA conformance** — breach rate per stage pinpoints where promises break.

## Tools
- Python: pm4py (full mining suite), or plain pandas as in `process_discovery.py`
- Commercial: Celonis / Signavio when org already pays

## Interpretation cautions
- The log shows what the SYSTEM recorded, not all work done.
- Frequent variants ≠ correct ones.
- Never present variant percentages without a process owner walkthrough first.
