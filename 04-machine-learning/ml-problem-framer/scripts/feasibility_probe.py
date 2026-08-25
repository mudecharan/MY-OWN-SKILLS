"""ml-problem-framer · feasibility probe: signal audit + class balance + rules baseline.
Usage: python feasibility_probe.py --data candidates.csv --target y
Quick pre-ML check BEFORE committing to a modeling project.
"""
import argparse

import numpy as np
import pandas as pd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--target", default="y")
    ap.add_argument("--date-col", default=None, help="for time-split signal audit")
    args = ap.parse_args()

    df = pd.read_csv(args.data)
    y = df[args.target]
    print(f"rows={len(df):,}  positive rate={y.mean():.1%}  positives={int(y.sum()):,}")

    if 0 < y.sum() < 100:
        print("⚠ <100 positives — likely insufficient for stable ML; collect more or reframe.")

    # single-feature signal audit (univariate AUC both directions)
    from sklearn.metrics import roc_auc_score
    rows = []
    for c in df.select_dtypes(include=np.number).columns:
        if c == args.target:
            continue
        mask = df[c].notna() & y.notna()
        if df.loc[mask, c].nunique() < 2:
            continue
        auc = roc_auc_score(y[mask], df.loc[mask, c])
        rows.append((c, max(auc, 1 - auc), abs(auc - 0.5) * 2))
    sig = (pd.DataFrame(rows, columns=["feature", "auc_best_dir", "signal"])
           .sort_values("signal", ascending=False))
    print("\n== Univariate signal audit (AUC vs target; >0.55 = usable signal) ==")
    print(sig.head(12).round(3).to_string(index=False))

    strong = (sig["auc_best_dir"] > 0.58).sum()
    print(f"\nFeatures with real standalone signal: {strong}")
    verdict = ("GO — enough signal to attempt modeling"
               if strong >= 2 else "WEAK — try better features/data before ML")
    print(f"Feasibility verdict: {verdict}")
    print("Next: define prediction-time snapshot & horizon; build rules-baseline to beat.")


if __name__ == "__main__":
    main()
