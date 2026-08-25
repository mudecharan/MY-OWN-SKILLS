"""requirements-elicitation-pro · interactive spec generator producing the sign-off template.
Usage: python spec_generator.py --title "Weekly revenue report" --output spec.md
Answer prompts; get a testable requirement specification ready for stakeholder sign-off.
"""
import argparse
from datetime import date
from pathlib import Path

QUESTIONS = [
    ("decision", "What DECISION will be made from this? (not 'see the data')"),
    ("action", "What will you DO differently when the number moves?"),
    ("consumers", "Who consumes it and what's their data literacy?"),
    ("frequency", "How often is it needed, and by when in the cycle?"),
    ("grain", "One row of output = one ___?"),
    ("measures", "Exact measures/formulas (numerator, denominator, exclusions)?"),
    ("dimensions", "Dimensions to break down by?"),
    ("filters", "Standing filters (exclude tests, returns, internal)?"),
    ("timezone", "Timezone & boundary rule (e.g., UTC day boundaries)?"),
    ("success", "How will we know this solved your problem?"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--output", default="requirement_spec.md")
    args = ap.parse_args()

    answers = {}
    print("Requirements elicitation — answer each prompt:\n")
    for key, q in QUESTIONS:
        answers[key] = input(f"- {q}\n  > ").strip()

    edge_cases = []
    print("\nEdge cases (enter blank line to finish):")
    while True:
        e = input("  edge case > ").strip()
        if not e:
            break
        edge_cases.append(e)

    moscow = {}
    print("\nPriorities for listed requirements (M/S/C or blank=defer):")
    for i in range(1, 6):
        r = input(f"  requirement R{i} (blank to stop) > ").strip()
        if not r:
            break
        moscow[f"R{i}"] = (r, input(f"    priority M/S/C > ").strip() or "C")

    lines = [
        f"# Requirement Specification — {args.title}",
        f"*Generated {date.today()} · status: DRAFT pending sign-off*\n",
        f"**Decision supported:** {answers['decision']}",
        f"**Action taken:** {answers['action']}",
        f"**Consumers:** {answers['consumers']}",
        f"**Frequency/deadline:** {answers['frequency']}",
        f"**Success definition:** {answers['success']}\n",
        "## Testable requirements",
    ]
    for rid, (text, prio) in moscow.items():
        lines.append(f"| {rid} | {text} | {prio} |")
    lines += ["", "## Grain & definitions",
              f"- Grain: one row = {answers['grain']}",
              f"- Measures: {answers['measures']}",
              f"- Dimensions: {answers['dimensions']}",
              f"- Filters: {answers['filters']}",
              f"- Timezone: {answers['timezone']}", "",
              "## Edge cases agreed"] + [f"- {e}" for e in edge_cases] + [
              "", "## Sign-off", "| Name | Role | Date |", "|---|---|---|",
              "|  |  |  |"]
    Path(args.output).write_text("\n".join(lines), encoding="utf-8")
    print(f"\nspec written -> {args.output} — no build starts before sign-off.")


if __name__ == "__main__":
    main()
