"""methodology-explainer · generates the three-layer methodology outline.
Usage: python methodology_outline.py --question "How did you measure churn?" \
         --approach "90-day inactivity window on usage data" --audience executive
"""
import argparse
import json
from pathlib import Path

LAYERS = {
    "executive": [
        ("Business question", "Restate the question in business terms, one sentence."),
        ("Approach in plain language", "Analogy allowed; no statistics vocabulary."),
        ("Why you can trust it", "One credibility point (validation, benchmark, or review)."),
    ],
    "manager": [
        ("Business question", ""),
        ("Approach", "Steps taken, in order, without formulas."),
        ("Data used", "Sources, period, exclusions."),
        ("Limitations", "Top two, with impact direction."),
    ],
    "technical": [
        ("Question & estimand", "Precise definition of what was measured."),
        ("Method", "Formulas/model specs/assumptions."),
        ("Data lineage", "Tables, filters, joins, transformation steps."),
        ("Validation", "Tests run, sensitivity checks, known weaknesses."),
        ("Reproducibility", "Where code/data live; how to re-run."),
    ],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--question", required=True)
    ap.add_argument("--approach", required=True)
    ap.add_argument("--audience", choices=list(LAYERS), default="executive")
    ap.add_argument("--out", default="methodology_outline.md")
    a = ap.parse_args()

    lines = [f"# Methodology Outline ({a.audience} depth)",
             f"Question: {a.question}", f"Approach: {a.approach}", ""]
    for i, (title, hint) in enumerate(LAYERS[a.audience], 1):
        lines.append(f"## Layer {i}: {title}")
        if hint:
            lines.append(f"*{hint}*")
        lines.append("- <fill in>\n")
    Path(a.out).write_text("\n".join(lines), encoding="utf-8")
    print(f"outline -> {a.out} - fill each layer, then transfer into the "
          f"writeup/slide templates in assets/")


if __name__ == "__main__":
    main()
