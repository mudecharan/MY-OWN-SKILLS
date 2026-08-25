"""churn-prediction-retention-kit · churn model with decile lift + save-value matrix.
Usage: python churn_model.py --data customers.csv --target churned --value_col mrr
Data: one row per customer; behavioral features computed as-of prediction date (no leakage!).
"""
import argparse

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--target", default="churned")
    ap.add_argument("--value-col", default="mrr")
    ap.add_argument("--save-rate", type=float, default=0.25, help="assumed save rate if intervened")
    ap.add_argument("--intervention-cost", type=float, default=50)
    a = ap.parse_args()

    df = pd.read_csv(a.data).dropna(subset=[a.target])
    y = df[a.target].astype(int)
    X = df.drop(columns=[c for c in [a.target, "customer_id"] if c in df.columns])
    X = pd.get_dummies(X, drop_first=True)

    # TIME-BASED split strongly recommended in production; stratified here
    Xtr, Xte, ytr, yte, dtr, dte = train_test_split(
        X, y, df, stratify=y, test_size=0.3, random_state=0)
    m = GradientBoostingClassifier(random_state=0).fit(Xtr, ytr)
    p = m.predict_proba(Xte)[:, 1]
    print(f"AUC={roc_auc_score(yte, p):.3f} · base rate={y.mean():.1%}\n")

    # decile lift table — the operational deliverable
    q = pd.qcut(pd.Series(p).rank(method="first"), 10, labels=False) + 1
    lift = pd.DataFrame({"decile": q, "churned": yte.values, "p": p}) \
        .groupby("decile").agg(n=("p", "size"), churn_rate=("churned", "mean"))
    lift["lift_x"] = lift["churn_rate"] / y.mean()
    print("== Decile table ==")
    print(lift.round(2).to_string())

    # save-value matrix: risk × value → intervention decision
    value = dte[a.value_col].values
    expected_save = p * a.save_rate * value * 12          # annualized value saved
    net = expected_save - np.where(p > 0.05, a.intervention_cost, 0)
    band = pd.cut(p, [0, .1, .25, .5, 1], labels=["low", "medium", "high", "critical"])
    matrix = pd.DataFrame({"risk": band, "expected_save": expected_save, "net_value": net}) \
        .groupby("risk", observed=True).agg(customers=("net_value", "size"),
                                            avg_net=("net_value", "mean"))
    print("\n== Save-value matrix (annualized) ==")
    print(matrix.round(0).to_string())
    print(f"\nIntervene where net>0. With cost=${a.intervention_cost}/contact and "
          f"save rate={a.save_rate:.0%}, focus on high/critical bands.")
    print("Drivers: extract SHAP per segment; only ACTIONABLE drivers become plays.")


if __name__ == "__main__":
    main()
