"""feature-engineering-workshop · leakage-safe feature builder + importance report.
Usage: python feature_builder.py --events events.csv --snapshot 2024-06-01 --target_col churned
Expects event log with columns: entity_id, event_ts, amount (optional), event_type.
"""
import argparse

import numpy as np
import pandas as pd


def build_features(events: pd.DataFrame, snapshot: str, freq="D") -> pd.DataFrame:
    """All windows END at the snapshot — structural leakage prevention."""
    t = pd.Timestamp(snapshot)
    ev = events.copy()
    ev["event_ts"] = pd.to_datetime(ev["event_ts"])
    ev = ev[ev["event_ts"] < t]                      # hard cutoff at prediction time
    ev["days_before_snapshot"] = (t - ev["event_ts"]).dt.days

    g = ev.groupby("entity_id")
    feats = pd.DataFrame({
        # recency / frequency / tenure
        "recency_days": g["days_before_snapshot"].min(),
        "tenure_days": g["days_before_snapshot"].max(),
        "n_events_30d": ev[ev.days_before_snapshot <= 30].groupby("entity_id").size(),
        "n_events_90d": ev[ev.days_before_snapshot <= 90].groupby("entity_id").size(),
        "amount_sum_90d": ev[ev.days_before_snapshot <= 90].groupby("entity_id")["amount"].sum(min_count=1),
        "amount_mean_all": g["amount"].mean(),
    })

    # velocity: recent activity vs trailing baseline
    feats["velocity_ratio"] = feats["n_events_30d"] * 3 / feats["n_events_90d"].replace(0, np.nan)

    # datetime cyclical encodings on last activity hour-of-day
    last = ev.sort_values("event_ts").groupby("entity_id").tail(1)
    hr = last["event_ts"].dt.hour
    feats["last_hr_sin"] = np.sin(2 * np.pi * hr / 24).values
    feats["last_hr_cos"] = np.cos(2 * np.pi * hr / 24).values

    return feats.reset_index()


def importance_report(feats: pd.DataFrame, target: pd.Series, name="model"):
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.inspection import permutation_importance
    from sklearn.model_selection import train_test_split

    X = feats.drop(columns=["entity_id"]).fillna(0)
    y = target.reindex(X.index)
    Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=0, test_size=0.25)
    m = GradientBoostingClassifier(random_state=0).fit(Xtr, ytr)
    pi = permutation_importance(m, Xte, yte, n_repeats=10, random_state=0)
    imp = (pd.Series(pi.importances_mean, index=X.columns)
           .sort_values(ascending=False))
    print(f"== {name}: permutation importance on held-out data ==")
    print((imp * 1000).round(2).to_string())
    print("\nAblation tip: drop one feature FAMILY (all rolling windows, all cyclical) "
          "and re-measure to price each family's contribution.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", required=True)
    ap.add_argument("--snapshot", required=True)
    ap.add_argument("--demo", action="store_true", help="run synthetic demo")
    a = ap.parse_args()

    if a.demo:
        rng = np.random.default_rng(0)
        ids = np.repeat(np.arange(300), rng.poisson(8, 300))
        events = pd.DataFrame({
            "entity_id": ids,
            "event_ts": pd.Timestamp("2024-01-01") + pd.to_timedelta(rng.integers(0, 150, len(ids)), unit="D"),
            "amount": rng.exponential(50, len(ids)),
            "event_type": rng.choice(["view", "buy"], len(ids)),
        })
        events.to_csv("events_demo.csv", index=False)

    events = pd.read_csv(a.events if not a.demo else "events_demo.csv")
    feats = build_features(events, a.snapshot)
    print(feats.describe().round(2).to_string())
