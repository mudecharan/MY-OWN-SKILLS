"""causal-inference-advisor · DiD + propensity matching starter implementations.
Usage:
  python causal_toolkit.py did --panel panel.csv --treat_col treated --post_col post --y outcome
  python causal_toolkit.py psm --data data.csv --treat_col treated --covars age,income,prior_spend
"""
import argparse

import numpy as np
import pandas as pd


def did(panel: pd.DataFrame, treat: str, post: str, y: str):
    """Difference-in-Differences via interaction OLS = 2x2 means difference."""
    import statsmodels.formula.api as smf
    m = smf.ols(f"{y} ~ {treat} * {post}", data=panel).fit(cov_type="HC1")
    print(m.summary().tables[1])
    eff = m.params.get(f"{treat}:{post}")
    ci = m.conf_int().loc[f"{treat}:{post}"]
    print(f"\nDiD effect: {eff:+.3f}  CI [{ci[0]:+.3f}, {ci[1]:+.3f}]")

    # pre-trend sanity: compare period-over-period changes before treatment
    pre = panel[panel[post] == 0]
    print("\nPre-trend check (means by group across pre-periods):")
    if "period" in panel.columns:
        print(pre.groupby([treat, "period"])[y].mean().unstack(0).to_string())


def psm(data: pd.DataFrame, treat: str, covars: list):
    from sklearn.linear_model import LogisticRegression
    d = data.dropna(subset=covars + [treat]).copy()
    X = pd.get_dummies(d[covars], drop_first=True).astype(float)
    ps = LogisticRegression(max_iter=2000).fit(X, d[treat]).predict_proba(X)[:, 1]
    d["ps"] = ps
    # caliper matching without replacement (greedy)
    treated = d[d[treat] == 1].sort_values("ps")
    control = d[d[treat] == 0].sort_values("ps").copy()
    matches, used = [], set()
    for _, row in treated.iterrows():
        free = control[~control.index.isin(used)]
        if free.empty:
            break
        best = (free["ps"] - row["ps"]).abs().idxmin()
        if abs(free.loc[best, "ps"] - row["ps"]) <= 0.05 * row["ps"]:   # caliper
            used.add(best)
            matches.append((row.name, best))
    print(f"Matched pairs: {len(matches)} of {len(treated)} treated")
    mt = d.loc[[a for a, _ in matches]]
    mc = d.loc[[b for _, b in matches]]

    # balance diagnostic: standardized bias before/after per covariate
    print("\nStandardized mean difference (want < 0.10 after):")
    for c in X.columns:
        def smd(a, b):
            return (a.mean() - b.mean()) / np.sqrt((a.var() + b.var()) / 2 + 1e-12)
        raw = smd(data.loc[data[treat] == 1, c].dropna(), data.loc[data[treat] == 0, c].dropna())
        adj = smd(mt[c], mc[c])
        flag = " ✅" if abs(adj) < 0.1 else " ❌"
        print(f"  {c:<25} raw={raw:+.2f} matched={adj:+.2f}{flag}")

    ycol = [c for c in d.columns if c not in covars + [treat, "ps"] and np.issubdtype(d[c].dtype, np.number)]
    if ycol:
        y = ycol[0]
        print(f"\nATT on '{y}' (matched diff-in-means): {mt[y].mean() - mc[y].mean():+.3f}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    dd = sub.add_parser("did")
    dd.add_argument("--panel", required=True)
    dd.add_argument("--treat_col", default="treated")
    dd.add_argument("--post_col", default="post")
    dd.add_argument("--y", default="outcome")

    pp = sub.add_parser("psm")
    pp.add_argument("--data", required=True)
    pp.add_argument("--treat_col", default="treated")
    pp.add_argument("--covars", required=True)

    a = ap.parse_args()
    if a.cmd == "did":
        did(pd.read_csv(a.panel), a.treat_col, a.post_col, a.y)
    else:
        psm(pd.read_csv(a.data), a.treat_col, [c.strip() for c in a.covars.split(",")])
