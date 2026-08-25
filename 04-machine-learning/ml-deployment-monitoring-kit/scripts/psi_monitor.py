"""ml-deployment-monitoring-kit · PSI drift monitor (the workhorse check).
Usage:
  reference: python psi_monitor.py --ref train_scores.csv --col score
  monitor:   python psi_monitor.py --ref train.csv --live today.csv --cols f1,f2,score
PSI: <0.1 stable · 0.1-0.25 moderate shift · >0.25 investigate.
"""
import argparse

import numpy as np
import pandas as pd


def psi(expected: np.ndarray, actual: np.ndarray, bins: int = 10) -> float:
    """Population Stability Index between two distributions."""
    edges = np.unique(np.quantile(expected, np.linspace(0, 1, bins + 1)))
    if len(edges) < 3:                       # constant feature
        return 0.0 if np.allclose(expected.mean(), actual.mean()) else float("inf")
    e = np.histogram(expected, bins=edges)[0] / len(expected)
    a = np.histogram(actual, bins=edges)[0] / max(1, len(actual))
    e, a = np.clip(e, 1e-6, None), np.clip(a, 1e-6, None)
    return float(np.sum((a - e) * np.log(a / e)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", required=True, help="training/reference data (csv)")
    ap.add_argument("--live", default=None, help="today's served data (csv)")
    ap.add_argument("--cols", default="", help="comma list; empty = all numeric in ref")
    a = ap.parse_args()

    ref = pd.read_csv(a.ref)
    cols = ([c.strip() for c in a.cols.split(",") if c.strip()]
            or list(ref.select_dtypes(include=np.number).columns))
    live = pd.read_csv(a.live) if a.live else None

    print(f"{'feature':<25} {'PSI':>8}  verdict")
    for c in cols:
        if c not in ref.columns:
            continue
        v = psi(ref[c].dropna().values,
                live[c].dropna().values) if live is not None else float("nan")
        if live is None:
            # self-check should be ~0; validates the metric plumbing
            v = psi(ref[c].dropna().values, ref[c].dropna().values)
        verdict = ("STABLE" if v < 0.1 else "moderate shift — watch"
                   if v < 0.25 else "INVESTIGATE — possible drift/upstream change")
        print(f"{c:<25} {v:>8.4f}  {verdict}")


if __name__ == "__main__":
    main()
