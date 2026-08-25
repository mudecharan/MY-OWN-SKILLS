"""seasonality-detector · STL decomposition, period verification, seasonal profile.
Usage: python seasonality_scan.py --data series.csv --date_col ds --y_col y [--period 7] [--plot stl.png]
"""
import argparse

import numpy as np
import pandas as pd


def acf(x, max_lag=40):
    x = (x - x.mean()) / x.std()
    return [1.0] + [np.corrcoef(x[:-k], x[k:])[0, 1] for k in range(1, min(max_lag, len(x) - 2))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--date-col", default="ds")
    ap.add_argument("--y-col", default="y")
    ap.add_argument("--period", type=int, default=None, help="suspected period; auto if omitted")
    ap.add_argument("--freq", default="D", choices=["D", "W", "M"], help="series frequency")
    ap.add_argument("--plot", default=None)
    a = ap.parse_args()

    df = pd.read_csv(a.data, parse_dates=[a.date_col])
    s = pd.Series(df[a.y_col].values,
                  index=pd.DatetimeIndex(df[a.date_col])).asfreq(a.freq).interpolate()

    # --- period verification via ACF peaks ---
    r = acf(s.values, 60)
    print("== ACF peaks (lag, autocorr) ==")
    for lag in range(2, len(r) - 1):
        if r[lag] > r[lag-1] and r[lag] >= r[lag+1] and r[lag] > 0.25:
            print(f"  lag={lag:>3}  r={r[lag]:+.2f}")
    period = a.period
    if period is None:
        candidates = [7 if a.freq == "D" else 4 if a.freq == "M" else 12]
        period = candidates[0]
    print(f"Using period = {period}")

    # --- STL decomposition ---
    try:
        from statsmodels.tsa.seasonal import STL
        res = STL(s, period=period, robust=True).fit()
        trend, seas, rem = res.trend, res.seasonal, res.resid
        # seasonal strength (Wang-Smith-Hyndman)
        fs = max(0.0, 1 - np.var(rem) / np.var(seas + rem))
        print(f"\nSeasonal strength: {fs:.2f}  (>0.6 = strong, model it; <0.2 = weak)")
    except ImportError:
        print("statsmodels not installed — install to enable STL")
        return

    # --- seasonal profile ---
    idx_attr = {"D": "dayofweek", "W": "weekday", "M": "month"}[a.freq]
    prof = (s - trend).groupby(getattr(s.index, idx_attr)).mean()
    lvl = s.mean()
    print(f"\n== Seasonal profile (% vs mean level) by {idx_attr} ==")
    print((prof / lvl * 100).round(1).to_string())

    # calendar effects quick check
    if a.freq == "D":
        wd = s.groupby(s.index.dayofweek).mean()
        print("\nDay-of-week means:", wd.round(1).to_dict())

    if a.plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(4, 1, figsize=(11, 10), sharex=True)
        axes[0].plot(s, color="#333"); axes[0].set_title("observed")
        axes[1].plot(trend, color="#e67e22"); axes[1].set_title("trend")
        axes[2].plot(seas, color="#4a9eed"); axes[2].set_title(f"seasonal (period={period})")
        axes[3].plot(rem, color="#999"); axes[3].set_title("remainder")
        fig.tight_layout(); fig.savefig(a.plot, dpi=130)
        print(f"Plot saved -> {a.plot}")


if __name__ == "__main__":
    main()
