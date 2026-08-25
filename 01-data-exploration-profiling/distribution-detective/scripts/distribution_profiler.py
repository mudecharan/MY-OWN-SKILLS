"""distribution-detective: shape, modality, tails, transformation comparison.
Usage: python distribution_profiler.py <data.csv> --cols revenue,session_min [--plot out.png]
"""
import argparse
import numpy as np
import pandas as pd
from scipy import stats


def profile(s: pd.Series, name: str) -> dict:
    s = s.dropna()
    sk = stats.skew(s)
    ku = stats.kurtosis(s)
    # Pareto check
    top5_share = s.nlargest(max(1, int(len(s) * 0.05))).sum() / max(1e-12, s.sum()) * 100
    # normality (subsample for speed)
    sample = s.sample(min(len(s), 5000), random_state=0)
    _, p_norm = stats.normaltest(sample)
    # bimodality via dip-ish heuristic: count KDE peaks coarsely
    counts, _ = np.histogram(sample, bins=40)
    smooth = pd.Series(counts).rolling(3, center=True).mean().fillna(0)
    peaks = int(((smooth.shift(1) < smooth) & (smooth.shift(-1) < smooth)).sum())

    # transformation lab (skew after transform)
    def skew_of(x):
        x = x[x > -1] if "log" in name else x
        return stats.skew(x)
    cands = {
        "raw": sk,
        "log1p": stats.skew(np.log1p(s.clip(lower=0))) if (s >= 0).all() else np.nan,
        "sqrt": stats.skew(np.sqrt(s.clip(lower=0))) if (s >= 0).all() else np.nan,
        "yeo-johnson": stats.skew(stats.yeojohnson(s)[0]),
    }
    best = min(cands, key=lambda k: abs(cands[k]))
    return {"var": name, "n": len(s), "skew": round(sk, 2), "kurt": round(ku, 2),
            "normal_p": f"{p_norm:.1e}", "peaks~": peaks, "top5%_value%": round(top5_share, 1),
            **{f"skew_{k}": round(v, 2) if v == v else None for k, v in cands.items()},
            "best_transform": best,
            "report_stat": "median+IQR" if abs(sk) > 1 else "mean±std"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--cols", required=True)
    ap.add_argument("--plot", default=None)
    a = ap.parse_args()
    df = pd.read_csv(a.path)
    cols = [c.strip() for c in a.cols.split(",")]

    cards = [profile(df[c], c) for c in cols]
    out = pd.DataFrame(cards)
    print(out.to_string(index=False))

    print("\nGuidance:")
    for card in cards:
        pareto = "PARETO FLAG — means misleading" if card["top5%_value%"] > 50 else ""
        mix = "MULTI-MODAL? hunt the hidden segment before transforming" if card["peaks~"] >= 2 else ""
        print(f"- {card['var']}: use {card['report_stat']}; prefer {card['best_transform']}. {pareto} {mix}")

    if a.plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(len(cols), 2, figsize=(11, 3.4 * len(cols)), squeeze=False)
        for i, c in enumerate(cols):
            s = df[c].dropna()
            axes[i][0].hist(np.log1p(s.clip(lower=0)), bins=50, color="#4a9eed")
            axes[i][0].set_title(f"{c} — histogram (log1p view)")
            stats.probplot(s.sample(min(len(s), 4000), random_state=0), plot=axes[i][1])
            axes[i][1].set_title(f"{c} — QQ vs normal")
        fig.tight_layout()
        fig.savefig(a.plot, dpi=130)
        print(f"\nPlots saved -> {a.plot}")


if __name__ == "__main__":
    main()
