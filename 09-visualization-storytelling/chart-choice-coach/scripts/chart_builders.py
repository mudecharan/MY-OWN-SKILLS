"""chart-choice-coach · house-style chart builders (matplotlib) with message titles.
Usage: python chart_builders.py --data data.csv --kind bar --x region --y revenue --title "EMEA leads revenue" [--out chart.png]
Kinds: bar | line | hist | scatter | stacked
"""
import argparse

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ACCENT = "#4a9eed"
GREY = "#8a8f98"
HILITE = "#e67e22"


def style(ax):
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    ax.tick_params(colors=GREY, labelsize=9)
    ax.yaxis.grid(True, alpha=.25)
    ax.set_axisbelow(True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--kind", required=True,
                    choices=["bar", "line", "hist", "scatter", "stacked"])
    ap.add_argument("--x"); ap.add_argument("--y"); ap.add_argument("--series")
    ap.add_argument("--highlight", default=None, help="bar category to emphasize")
    ap.add_argument("--title", required=True, help="message title (the takeaway!)")
    ap.add_argument("--out", default="chart.png")
    a = ap.parse_args()
    df = pd.read_csv(a.data)

    fig, ax = plt.subplots(figsize=(8, 4.5))
    if a.kind == "bar":
        s = df.groupby(a.x)[a.y].sum().sort_values(ascending=False)
        colors = [HILITE if (a.highlight and str(i) == a.highlight) else ACCENT for i in s.index]
        s.plot.bar(ax=ax, color=colors)
        style(ax); ax.set_title(f"{a.title}\n", loc="left", fontweight="bold")
    elif a.kind == "line":
        for key, g in df.groupby(a.series or a.x):
            ax.plot(g[a.x], g[a.y], label=key)
        ax.legend(frameon=False)
        style(ax); ax.set_title(a.title, loc="left", fontweight="bold")
    elif a.kind == "hist":
        df[a.y].plot.hist(bins=30, color=ACCENT, ax=ax)
        style(ax); ax.set_title(a.title, loc="left", fontweight="bold")
    elif a.kind == "scatter":
        ax.scatter(df[a.x], df[a.y], s=18, alpha=.6, color=ACCENT)
        style(ax); ax.set_title(a.title, loc="left", fontweight="bold")
    elif a.kind == "stacked":
        p = df.pivot_table(index=a.x, columns=a.series, values=a.y, aggfunc="sum").fillna(0)
        p.apply(lambda r: 100 * r / r.sum(), axis=1).plot.bar(stacked=True, ax=ax,
                                                              colormap="viridis")
        style(ax); ax.set_title(a.title, loc="left", fontweight="bold")

    fig.tight_layout()
    fig.savefig(a.out, dpi=150)
    print(f"saved -> {a.out}")
    print("Checklist applied: sorted bars? zero baseline? takeaway title? one color meaning?")


if __name__ == "__main__":
    main()
