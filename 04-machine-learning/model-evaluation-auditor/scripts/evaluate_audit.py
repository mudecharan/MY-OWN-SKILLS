"""model-evaluation-auditor · honest evaluation: calibration, threshold economics, slices.
Usage: python evaluate_audit.py --data preds.csv --y_col y --p_col p [--segment_col region]
preds.csv needs: true label column, predicted probability column, optional segments.
"""
import argparse

import numpy as np
import pandas as pd


def calibration_table(y, p, bins=10):
    q = pd.qcut(p.rank(method="first"), bins, labels=False)
    t = pd.DataFrame({"bin": q, "y": y, "p": p}).groupby("bin").agg(
        n=("y", "size"), actual=("y", "mean"), predicted=("p", "mean"))
    return t


def brier(y, p):
    return np.mean((p - y) ** 2)


def threshold_economics(y, p, fp_cost=1, fn_cost=10, tp_value=20):
    rows = []
    for thr in np.linspace(0.05, 0.95, 19):
        pred = (p >= thr).astype(int)
        tp = ((pred == 1) & (y == 1)).sum()
        fp = ((pred == 1) & (y == 0)).sum()
        fn = ((pred == 0) & (y == 1)).sum()
        value = tp * tp_value - fp * fp_cost - fn * fn_cost
        rows.append((thr, tp, fp, fn, value))
    best = max(rows, key=lambda r: r[-1])
    return pd.DataFrame(rows, columns=["thr", "tp", "fp", "fn", "net_value"]), best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--y-col", default="y")
    ap.add_argument("--p-col", default="p")
    ap.add_argument("--segment-col", default=None)
    ap.add_argument("--fp-cost", type=float, default=1)
    ap.add_argument("--fn-cost", type=float, default=10)
    a = ap.parse_args()

    df = pd.read_csv(a.data)
    y, p = df[a.y_col].astype(int), df[a.p_col]

    print(f"ROC-AUC: {__import__('sklearn.metrics', fromlist=['roc_auc_score']).roc_auc_score(y, p):.3f}")
    print(f"Brier score: {brier(y, p):.4f} (lower=better; compare vs base-rate model)")

    print("\nCalibration by decile (predicted should track actual):")
    print(calibration_table(y, p).round(3).to_string())

    econ, best = threshold_economics(y, p, a.fp_cost, a.fn_cost)
    print(f"\nProfit-maximizing operating point: threshold={best[0]:.2f} "
          f"(tp={best[1]}, fp={best[2]}, fn={best[3]}, net={best[4]:,.0f})")
    print("NOTE: default 0.5 is almost never optimal — use the cost matrix.")

    if a.segment_col:
        from sklearn.metrics import roc_auc_score
        print(f"\nSlice performance by {a.segment_col}:")
        for seg, sub in df.groupby(a.segment_col):
            if sub[a.y_col].nunique() > 1:
                print(f"  {seg:<20} n={len(sub):>7,} AUC={roc_auc_score(sub[a.y_col], sub[a.p_col]):.3f}")
        print("A model great on average but failing a major slice WILL fail publicly.")


if __name__ == "__main__":
    main()
