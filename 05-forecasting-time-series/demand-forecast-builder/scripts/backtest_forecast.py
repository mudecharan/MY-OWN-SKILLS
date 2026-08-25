"""demand-forecast-builder · rolling-origin backtest + forecast with quantiles.
Usage: python backtest_forecast.py --data series.csv --date_col ds --y_col y --horizon 30 [--plot fc.png]
series.csv needs a date column and a numeric target. Benchmarks + ETS + seasonal-naive.
"""
import argparse

import numpy as np
import pandas as pd


def seasonal_naive(train, horizon, season=7):
    vals = train["y"].values
    if len(vals) < season:
        return np.repeat(vals[-1], horizon)
    return np.array([vals[-season + i % season] for i in range(horizon)])


def naive_drift(train, horizon):
    y = train["y"].values
    slope = (y[-1] - y[0]) / max(1, len(y) - 1)
    return y[-1] + slope * np.arange(1, horizon + 1)


def ets_forecast(train, horizon):
    try:
        from statsmodels.tsa.holtwinters import ExponentialSmoothing
        m = ExponentialSmoothing(train["y"], trend="add",
                                 seasonal="add", seasonal_periods=min(7, max(2, len(train)//3))).fit()
        return np.asarray(m.forecast(horizon))
    except Exception:
        return naive_drift(train, horizon)


def quantile_band(fit_resid_std: float, horizon: float) -> dict:
    """P10/P90 widen with sqrt(horizon) — honest uncertainty growth."""
    w = fit_resid_std * np.sqrt(np.arange(1, horizon + 1))
    return {"p10": -1.28 * w, "p90": +1.28 * w}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--date-col", default="ds")
    ap.add_argument("--y-col", default="y")
    ap.add_argument("--horizon", type=int, default=30)
    ap.add_argument("--folds", type=int, default=3)
    ap.add_argument("--plot", default=None)
    a = ap.parse_args()

    df = pd.read_csv(a.data, parse_dates=[a.date_col]).rename(
        columns={a.date_col: "ds", a.y_col: "y"}).sort_values("ds").reset_index(drop=True)

    # ---- rolling-origin backtest ----
    methods = {"naive_drift": naive_drift, "seasonal_naive": seasonal_naive, "ets": ets_forecast}
    scores = {k: [] for k in methods}
    fold_len = len(df) // (a.folds + 1)
    for f in range(a.folds):
        cut = fold_len * (f + 1) + min(a.horizon, len(df) - fold_len * (f + 1))
        cut = min(cut, len(df))
        train, test = df.iloc[:cut], df.iloc[cut:cut + a.horizon]
        if len(test) == 0:
            continue
        for name, fn in methods.items():
            pred = fn(train, len(test))[:len(test)]
            err = pred - test["y"].values
            scores[name].append(np.mean(np.abs(err)))

    print("== Rolling-origin backtest (MAE per method; must beat benchmarks!) ==")
    for name, errs in scores.items():
        if errs:
            print(f"  {name:<15} MAE={np.mean(errs):,.1f}")

    best = min((k for k in methods if scores[k]), key=lambda k: np.mean(scores[k]))
    print(f"  --> selected: {best}")

    # ---- final forecast with uncertainty band ----
    fc = methods[best](df, a.horizon)
    resid_std = float(scores.get(best) and np.mean(scores[best])) or df["y"].std()
    band = quantile_band(resid_std, a.horizon)
    future = pd.DataFrame({
        "ds": pd.date_range(df["ds"].iloc[-1] + pd.Timedelta(days=1), periods=a.horizon),
        "forecast": fc,
        "p10": fc + band["p10"], "p50": fc, "p90": fc + band["p90"],
    })
    print("\n== Forecast head ==")
    print(future.head(7).round(1).to_string(index=False))

    if a.plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(11, 4))
        ax.plot(df["ds"].tail(120), df["y"].tail(120), label="actual", color="#333")
        ax.plot(future["ds"], future["p50"], label="forecast", color="#4a9eed")
        ax.fill_between(future["ds"], future["p10"], future["p90"], alpha=.25,
                        color="#4a9eed", label="P10–P90")
        ax.legend(); fig.tight_layout(); fig.savefig(a.plot, dpi=130)
        print(f"\nPlot saved -> {a.plot}")


if __name__ == "__main__":
    main()
