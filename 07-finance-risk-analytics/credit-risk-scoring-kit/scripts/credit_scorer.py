"""credit-risk-scoring-kit · scorecard-style PD model with calibration + cut-off curves.
Usage: python credit_scorer.py --data loans.csv --target default_12m --features age,income,util,dpd_hist
Data needs: binary default outcome, numeric features available at decision time.
"""
import argparse

import numpy as np
import pandas as pd
from sklearn.calibration import CalibratedClassifierCV, calibration_curve
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--target", default="default_12m")
    ap.add_argument("--features", required=True)
    a = ap.parse_args()

    df = pd.read_csv(a.data).dropna()
    y, X = df[a.target].astype(int), df[[c.strip() for c in a.features.split(",")]]

    # TIME-BASED split when a date column exists; stratified fallback here
    Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, test_size=0.3, random_state=0)

    base = GradientBoostingClassifier(random_state=0)
    model = CalibratedClassifierCV(base, method="isotonic", cv=3).fit(Xtr, ytr)
    p = model.predict_proba(Xte)[:, 1]

    print(f"Discrimination: AUC={roc_auc_score(yte, p):.3f} "
          f"(ranking only; calibration matters for decisions)")
    print(f"Mean predicted PD={p.mean():.3f} vs actual default rate={yte.mean():.3f} (should match)")

    frac, mean_p = calibration_curve(yte, p, n_bins=8)
    print("\nCalibration (predicted PD vs realized):")
    for mp, f in zip(mean_p, frac):
        print(f"  predicted={mp:.3f}  realized={f:.3f}  gap={f-mp:+.3f}")

    # cut-off economics: approval rate vs expected loss
    lgd = 0.8  # loss given default assumption — set with finance
    print("\nCut-off trade-off (per 1,000 applicants):")
    print(f"{'PD cut':>8} {'approve%':>9} {'bad caught%':>12} {'expected loss':>14}")
    for cut in np.quantile(p, [0.1, 0.25, 0.5, 0.75, 0.9]):
        approved = p < cut
        loss = (p[~approved].sum() * lgd)
        print(f"{cut:>8.3f} {approved.mean():>9.1%} {1 - approved.mean():>12.1%} {loss:>14.1f}")
    print("\nChoose the operating point with finance from the profit curve, not by AUC.")
    print("Governance: attach reason codes (top SHAP drivers) for every decline.")


if __name__ == "__main__":
    main()
