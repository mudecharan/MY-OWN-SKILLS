"""trend-decomposition-analyst · trend vs noise verdict, change points, scenario bands.
Usage: python trend_analysis.py --data series.csv --date_col ds --y_col y [--plot tr.png]
"""
import argparse

import numpy as np
import pandas as pd


def noise_floor(s: pd.Series) -> dict:
    """Is a claimed 'trend' even bigger than the noise?"""
    wow = s.diff().dropna()
    return {"cv": s.std() / max(1e-9, s.mean()), "wow_std": wow.std(),
            "wow_cv%": 100 * wow.std() / max(1e-9, abs(s.mean()))}


def changepoints_cusum(s: pd.Series, threshold=4.0):
    """Simple CUSUM on detrended residuals; returns candidate break indices."""
    resid = (s - s.rolling(max(8, len(s)//6), center=True).mean()).fillna(0)
    z = (resid - resid.mean()) / (resid.std() or 1e-9)
    cp, cum, run_start = [], 0.0, None
    for i, v in enumerate(z):
        if abs(cum + v) < abs(cum):
            pass
        cum += v
        if run_start is None and abs(v) > threshold:
            run_start = i
        if run_start is not None and abs(v) < threshold * 0.3:
            cp.append((run_start, i)); run_start = None; cum = 0
    return cp


def growth_by_segment(s: pd.Series, breaks: list) -> pd.DataFrame:
    bounds = [0] + [b for pair in breaks for b in pair] + [len(s)]
    bounds = sorted(set(bounds))
    rows = []
    for lo, hi in zip(bounds[:-1], bounds[1:]):
        seg = s.iloc[lo:hi]
        if len(seg) >= 8:
            slope = np.polyfit(np.arange(len(seg)), seg.values, 1)[0]
            rows.append({"window": f"{seg.index[0].date()} to {seg.index[-1].date()}",
                         "n": len(seg), "level": round(seg.mean(), 1),
                         "slope_per_period": round(slope, 2),
                         "growth_%/period": round(100 * slope / max(1e-9, seg.mean()), 2)})
    return pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--date-col", default="ds")
    ap.add_argument("--y-col", default="y")
    ap.add_argument("--horizon", type=int, default=8)
    ap.add_argument("--plot", default=None)
    a = ap.parse_args()

    df = pd.read_csv(a.data, parse_dates=[a.date_col])
    s = pd.Series(df[a.y_col].values, index=pd.DatetimeIndex(df[a.date_col])).asfreq("D").interpolate()

    nf = noise_floor(s)
    print(f"== Noise floor ==\n  CV={nf['cv']:.2f} | WoW volatility ~{nf['wow_cv%']:.1f}% of level")
    print("  A claimed 'trend' must exceed this per-period movement to be evidence.")

    breaks = changepoints_cusum(s)
    print(f"\n== Change-point candidates ==")
    for start, end in breaks:
        print(f"  around {s.index[start].date()} (run {start}–{end})")
    if not breaks:
        print("  none above threshold — stable regime")

    table = growth_by_segment(s, breaks)
    print("\n== Growth by stable segment ==")
    print(table.to_string(index=False))

    # Simpson's-paradox guard note
    print("\nGuard: re-run per key segment before headline claims "
          "(aggregate trends can be one segment dragging the rest).")

    # scenario projection from last stable segment
    last_slope = table["slope_per_period"].iloc[-1] if len(table) else 0
    base = s.iloc[-1]
    h = np.arange(1, a.horizon + 1)
    proj = pd.DataFrame({
        "step": h,
        "bear": base + 0.5 * last_slope * h - 1.28 * nf["wow_std"] * np.sqrt(h),
        "base": base + last_slope * h,
        "bull": base + 1.5 * last_slope * h + 1.28 * nf["wow_std"] * np.sqrt(h),
    })
    print("\n== Scenario projection (assumption: last-segment slope persists) ==")
    print(proj.round(1).to_string(index=False))
    print("Linear extrapolation beyond 1–2 periods is NOT justified without stated assumptions.")

    if a.plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(11, 4))
        ax.plot(s.index, s.values, color="#333")
        for _, row in table.iterrows():
            ax.axvline(pd.Timestamp(row["window"].split("→")[1]), color="red", ls="--", alpha=.5)
        ax.set_title("series with change points")
        fig.tight_layout(); fig.savefig(a.plot, dpi=130)
        print(f"\nPlot saved -> {a.plot}")


if __name__ == "__main__":
    main()
