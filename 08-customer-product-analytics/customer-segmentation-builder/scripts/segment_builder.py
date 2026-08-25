"""customer-segmentation-builder · RFM scoring + k-means with stability checks.
Usage: python segment_builder.py --tx transactions.csv --customer_col customer_id --date_col date --amount_col amount [--k 5]
"""
import argparse

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


def rfm(tx, cust, date, amt):
    tx = tx.copy()
    tx[date] = pd.to_datetime(tx[date])
    snap = tx[date].max() + pd.Timedelta(days=1)
    g = tx.groupby(cust)
    rfm_df = pd.DataFrame({
        "recency_days": (snap - g[date].max()).dt.days,
        "frequency": g.size(),
        "monetary": g[amt].sum(),
    })
    for c in ["recency_days", "frequency", "monetary"]:
        rfm_df[f"{c}_q"] = pd.qcut(rfm_df[c].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]).astype(int)
    rfm_df["R"] = 6 - rfm_df["recency_days_q"]          # low recency days = best
    rfm_df["rfm_score"] = rfm_df["R"].astype(str) + rfm_df["frequency_q"].astype(str) + rfm_df["monetary_q"].astype(str)
    return rfm_df


def kmeans_segments(rfm_df, k=None):
    X = StandardScaler().fit_transform(np.log1p(rfm_df[["recency_days", "frequency", "monetary"]]))
    if k is None:
        print("k selection (silhouette):")
        for kk in range(3, 8):
            s = silhouette_score(X, KMeans(n_clusters=kk, n_init=10, random_state=0).fit_predict(X))
            print(f"  k={kk}: {s:.3f}")
        k = 5
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit_predict(X)

    # stability: bootstrap re-fit agreement (rough proxy via split-half ARI)
    from sklearn.metrics import adjusted_rand_score
    rng = np.random.default_rng(0)
    aris = []
    for _ in range(5):
        idx = rng.choice(len(X), len(X) // 2, replace=False)
        m1 = KMeans(k, n_init=10, random_state=1).fit(X[idx])
        m2 = KMeans(k, n_init=10, random_state=2).fit(X[idx])
        aris.append(adjusted_rand_score(m1.labels_, m2.labels_))
    print(f"Split-half stability ARI: {np.mean(aris):.2f} (>0.6 acceptable)")

    seg = rfm_df.copy()
    seg["cluster"] = km
    profile = seg.groupby("cluster").agg(
        n=("recency_days", "size"),
        recency_med=("recency_days", "median"),
        freq_med=("frequency", "median"),
        monetary_med=("monetary", "median"),
        value_share=("monetary", lambda s: s.sum() / seg["monetary"].sum()),
    )
    print("\n== Cluster profile ==")
    print(profile.round(2).to_string())
    return seg


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--tx", required=True)
    ap.add_argument("--customer-col", default="customer_id")
    ap.add_argument("--date-col", default="date")
    ap.add_argument("--amount-col", default="amount")
    ap.add_argument("--k", type=int, default=None)
    a = ap.parse_args()
    tx = pd.read_csv(a.tx)
    r = rfm(tx, a.customer_col, a.date_col, a.amount_col)
    print(r[["recency_days", "frequency", "monetary", "rfm_score"]].describe().round(1).to_string())
    kmeans_segments(r, a.k)
