"""process-mapper-analyst · event-log analysis: variants, bottlenecks, rework.
Usage: python process_discovery.py --log events.csv --case_col case_id --act_col activity --ts_col timestamp
events.csv: one row per activity execution with case id, activity name, timestamp (ISO), optional resource.
"""
import argparse

import pandas as pd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", required=True)
    ap.add_argument("--case-col", default="case_id")
    ap.add_argument("--act-col", default="activity")
    ap.add_argument("--ts-col", default="timestamp")
    a = ap.parse_args()

    df = pd.read_csv(a.log, parse_dates=[a.ts_col])
    df = df.sort_values([a.case_col, a.ts_col])

    # --- 1) flow variants ---
    df["seq"] = df.groupby(a.case_col).cumcount()
    variants = (df.groupby(a.case_col)[a.act_col].apply(lambda s: " > ".join(s))
                  .value_counts())
    n_cases = variants.sum()
    print("== Flow variants (as actually executed) ==")
    cum = 0
    for v, c in variants.head(8).items():
        cum += c
        print(f"  {100*c/n_cases:5.1f}% ({c:>4})  {v[:110]}")
    print(f"  top-8 coverage: {100*cum/n_cases:.1f}% of {n_cases} cases; "
          f"{len(variants)} distinct variants total")

    # --- 2) waiting time between steps ---
    df["prev_ts"] = df.groupby(a.case_col)[a.ts_col].shift()
    df["wait_h"] = (df[a.ts_col] - df["prev_ts"]).dt.total_seconds() / 3600
    wait = df.groupby(a.act_col)["wait_h"].agg(["count", "median", "mean"]).dropna()
    wait = wait.sort_values("mean", ascending=False)
    print("\n== Waiting-time league table (hours before this step starts) ==")
    print(wait.round(1).head(10).to_string())

    # --- 3) rework: repeated activities within a case ---
    repeats = df.groupby([a.case_col, a.act_col]).size()
    rework = repeats[repeats > 1].value_counts().sort_index()
    print("\n== Rework (activities repeated within a case) ==")
    if len(rework):
        for times, n_cases_aff in rework.items():
            print(f"  {n_cases_aff} cases had an activity executed {times}x")
    else:
        print("  none detected")

    # --- 4) case duration ---
    dur = df.groupby(a.case_col)[a.ts_col].agg(["min", "max"])
    dur_h = (dur["max"] - dur["min"]).dt.total_seconds() / 3600
    print("\n== Case duration (hours) ==")
    print(dur_h.describe(percentiles=[0.5, 0.9]).round(1).to_string())


if __name__ == "__main__":
    main()
