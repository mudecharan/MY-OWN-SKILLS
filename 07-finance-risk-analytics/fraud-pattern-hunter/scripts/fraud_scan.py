"""fraud-pattern-hunter · velocity rules + isolation forest discovery + link analysis.
Usage: python fraud_scan.py --tx transactions.csv
transactions.csv: tx_id, account_id, ts, amount, device_id, ip_country, billing_country, is_fraud (optional label)
"""
import argparse

import numpy as np
import pandas as pd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tx", required=True)
    a = ap.parse_args()
    df = pd.read_csv(a.tx, parse_dates=["ts"]).sort_values("ts")

    # ---- known-pattern screening ----
    df["geo_mismatch"] = df.get("ip_country") != df.get("billing_country")
    vel = (df.sort_values("ts")
             .groupby("device_id")["account_id"]
             .rolling("24h").apply(lambda s: s.nunique(), raw=False)
             .rename("cards_per_device_24h").reset_index())
    df = df.merge(vel, on="account_id", how="left") if "account_id" in vel.columns else df

    near = df[(df["amount"] >= 90) & (df["amount"] < 100)]
    print("== Rule screen ==")
    print(f"geo mismatch rate: {df['geo_mismatch'].mean():.1%}")
    print(f"structuring band ($90-99): {len(near):,} tx ({100*len(near)/len(df):.1f}%)")

    # ---- unsupervised discovery ----
    feats = pd.DataFrame({
        "amount_z": np.abs((df["amount"] - df["amount"].mean()) / df["amount"].std()),
        "hour": df["ts"].dt.hour,
        "geo_mismatch": df["geo_mismatch"].astype(int),
        "amt_vs_account_avg": df["amount"] / df.groupby("account_id")["amount"].transform("mean"),
    }).fillna(0)
    from sklearn.ensemble import IsolationForest
    iso = IsolationForest(n_estimators=200, contamination=0.02, random_state=0).fit(feats)
    df["anomaly_score"] = -iso.score_samples(feats)
    top = df.nlargest(10, "anomaly_score")
    print("\n== Isolation-forest top 10 (human-label these before acting) ==")
    cols = [c for c in ["tx_id", "account_id", "ts", "amount", "is_fraud"] if c in top.columns]
    print(top[cols + ["anomaly_score"]].to_string(index=False))

    # ---- link analysis: shared devices across accounts ----
    if {"device_id", "account_id"} <= set(df.columns):
        links = (df.groupby("device_id")["account_id"].nunique()
                   .sort_values(ascending=False))
        rings = links[links > 2]
        print(f"\n== Link analysis == devices used by >2 accounts: {len(rings)} "
              f"(covering {df[df.device_id.isin(rings.index)]['account_id'].nunique()} accounts)")
        print(rings.head(5).to_string())

    if "is_fraud" in df.columns:
        hit = df.nlargest(max(1, int(len(df)*0.02)), "anomaly_score")
        prec = hit["is_fraud"].mean()
        rec = hit["is_fraud"].sum() / max(1, df["is_fraud"].sum())
        print(f"\nDetector backtest @2% review queue: precision={prec:.0%} recall={rec:.0%}")


if __name__ == "__main__":
    main()
