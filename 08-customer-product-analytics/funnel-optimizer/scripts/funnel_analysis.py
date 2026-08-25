"""funnel-optimizer · funnel baseline, opportunity ranking, segment paradox check.
Usage: python funnel_analysis.py --events events.csv --user_col user_id --ts_col ts --steps visit,signup,activate,purchase
events.csv: one row per user-step occurrence (first occurrence per step is used).
"""
import argparse

import numpy as np
import pandas as pd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", required=True)
    ap.add_argument("--user-col", default="user_id")
    ap.add_argument("--ts-col", default="ts")
    ap.add_argument("--steps", required=True, help="comma list in funnel order")
    ap.add_argument("--segment-cols", default="", help="optional comma list for paradox check")
    a = ap.parse_args()

    steps = [s.strip() for s in a.steps.split(",")]
    df = pd.read_csv(a.events, parse_dates=[a.ts_col])
    first = (df[df["event"].isin(steps)]
             .sort_values(a.ts_col)
             .drop_duplicates([a.user_col, "event"]))
    wide = first.pivot(index=a.user_col, columns="event", values=a.ts_col)

    # reached-step flags respecting ORDER
    reach = pd.DataFrame(index=wide.index)
    prev = None
    for s in steps:
        if s not in wide.columns:
            print(f"WARNING: step '{s}' not found in events"); return
        reach[s] = wide[s].notna() if prev is None else (wide[s].notna() & reach[prev])
        prev = s

    n = len(reach)
    rows, cum = [], n
    for i, s in enumerate(steps):
        r = int(reach[s].sum())
        drop = cum - r
        # exit-value proxy: downstream steps remaining
        downstream_value = len(steps) - i - 1
        rows.append({"step": s, "reached": r, "% of entry": round(100 * r / n, 1),
                     "drop_from_prev": drop,
                     "drop_%": round(100 * drop / max(1, cum), 1),
                     "downstream_steps_lost": downstream_value})
        cum = r
    table = pd.DataFrame(rows)
    table["opportunity_score"] = table["drop_from_prev"] * table["downstream_steps_lost"]
    print("== Funnel baseline (ordered) ==")
    print(table.to_string(index=False))
    print("\nPriority = biggest drop × most downstream value at stake.")

    # time-to-convert stalls
    print("\n== Median time to next step (hours; long stalls = friction) ==")
    for i in range(len(steps) - 1):
        dt = (wide[steps[i + 1]] - wide[steps[i]]).dt.total_seconds() / 3600
        print(f"  {steps[i]} -> {steps[i+1]:<12} median={dt.median():.1f}h")

    # Simpson's paradox check per segment
    for col in [c.strip() for c in a.segment_cols.split(",") if c.strip()]:
        if col not in df.columns:
            continue
        seg_map = df.groupby(a.user_col)[col].last()
        print(f"\n== Step conversion by {col} (watch for reversals vs aggregate) ==")
        for seg, idx in seg_map.groupby(seg_map).groups.items():
            sub = reach.loc[idx]
            conv = [100 * sub[s].sum() / max(1, sub[steps[0]].sum()) for s in steps[1:]]
            print(f"  {str(seg):<15} " + " ".join(f"{c:5.1f}%" for c in conv))


if __name__ == "__main__":
    main()
