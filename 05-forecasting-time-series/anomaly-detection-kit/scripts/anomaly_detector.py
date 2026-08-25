"""anomaly-detection-kit · seasonality-aware detector with persistence + calibration.
Usage: python anomaly_detector.py --data series.csv --date_col ds --y_col y [--persistence 2] [--plot an.png]
Method: STL residuals + robust (MAD) bands; backtests precision/recall on injected anomalies.
"""
import argparse

import numpy as np
import pandas as pd


def detect(s: pd.Series, period=7, z_thresh=3.0):
    from statsmodels.tsa.seasonal import STL
    res = STL(s, period=period, robust=True).fit()
    resid = res.resid
    med = np.median(resid)
    mad = np.median(np.abs(resid - med)) * 1.4826 or 1e-9
    rz = (resid - med) / mad
    flags = pd.Series(rz.abs() > z_thresh, index=s.index)
    return flags, rz, resid


def apply_persistence(flags: pd.Series, n: int) -> pd.Series:
    """Fire only when N consecutive breaches — kills single-point noise."""
    if n <= 1:
        return flags
    run = flags.rolling(n).sum()
    return run >= n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--date-col", default="ds")
    ap.add_argument("--y-col", default="y")
    ap.add_argument("--period", type=int, default=7)
    ap.add_argument("--z", type=float, default=3.0)
    ap.add_argument("--persistence", type=int, default=2)
    ap.add_argument("--inject-test", action="store_true",
                    help="inject 5 synthetic spikes and report precision/recall")
    ap.add_argument("--plot", default=None)
    a = ap.parse_args()

    df = pd.read_csv(a.data, parse_dates=[a.date_col])
    s = pd.Series(df[a.y_col].values, index=pd.DatetimeIndex(df[a.date_col])).asfreq("D").interpolate()

    truth = None
    if a.inject_test:
        rng = np.random.default_rng(7)
        idx = rng.choice(len(s), 5, replace=False)
        truth = pd.Series(False, index=s.index)
        truth.iloc[idx] = True
        s2 = s.copy()
        s2.iloc[idx] *= 1.8
        s = s2

    raw_flags, rz, resid = detect(s, a.period, a.z)
    alerts = apply_persistence(raw_flags, a.persistence)

    print(f"Raw breaches: {raw_flags.sum()}  ->  after persistence({a.persistence}): {alerts.sum()}")
    top = rz[raw_flags].abs().sort_values(ascending=False).head(10)
    print("\nTop flagged points:")
    for ts, v in top.items():
        print(f"  {ts.date()}  |robust-z|={v:.1f}  value={s[ts]:,.0f}")

    if truth is not None:
        tp = int((alerts & truth).sum()); fp = int((alerts & ~truth).sum()); fn = int((~alerts & truth).sum())
        prec = tp / max(1, tp + fp); rec = tp / max(1, tp + fn)
        print(f"\nBacktest vs injected: precision={prec:.0%} recall={rec:.0%} "
              f"(target alert volume: humans can handle ~few/day)")

    if a.plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(11, 4))
        ax.plot(s.index, s.values, color="#333", label="series")
        ax.scatter(s.index[alerts], s[alerts], color="red", zorder=5, label="alerts")
        band_hi = s.rolling(a.period*4, center=True).mean() + 2*s.diff().std()
        ax.legend(); fig.tight_layout(); fig.savefig(a.plot, dpi=130)
        print(f"\nPlot saved -> {a.plot}")


if __name__ == "__main__":
    main()
