"""executive-narrative-writer · pyramid narrative linter.
Usage: python narrative_linter.py --deck deck.md
Checks deck outline (one slide per line: 'Title | element') for pyramid-principle violations:
topic-only titles, hedges, jargon, missing ask.
"""
import argparse
import re
from pathlib import Path

HEDGES = ["might", "possibly", "perhaps", "maybe", "it seems"]
JARGON = ["utilize", "leverage ", "synergy", "paradigm", "holistic",
          "statistically significant", "p-value"]
TOPIC_STARTS = ("analysis of", "overview of", "summary of", "q1", "q2", "q3", "q4",
                "report on", "update on")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--deck", required=True)
    args = ap.parse_args()
    lines = [l.strip() for l in Path(args.deck).read_text(encoding="utf-8").splitlines()
             if l.strip() and not l.startswith("#")]

    issues = []
    for i, line in enumerate(lines, 1):
        title = line.split("|")[0].strip()
        low = title.lower()
        if low.startswith(TOPIC_STARTS):
            issues.append((i, f"'{title[:50]}' — TOPIC title. Rewrite as the takeaway/action."))
        if any(h in low for h in HEDGES):
            issues.append((i, f"'{title[:40]}' — hedge word. Commit or cut the claim."))
        if any(j in low for j in JARGON):
            issues.append((i, f"'{title[:40]}' — jargon/p-stats up front. Translate to business units."))

    full = "\n".join(lines).lower()
    if not re.search(r"(decis|approv|by .*\d{4}|next week|deadline)", full):
        issues.append((len(lines), "No ASK detected — add decision needed / owner / deadline."))

    if issues:
        print("PYRAMID LINT FINDINGS:")
        for i, msg in issues:
            print(f"  slide/line {i}: {msg}")
    else:
        print("Clean: action titles, no hedges/jargon, explicit ask present.")
    print(f"\n{len(lines)} slides reviewed. Rule: one message per slide; answer first.")


if __name__ == "__main__":
    main()
