"""correlation-radar: full association sweep + multicollinearity audit.
Usage: python correlation_sweep.py <data.csv> [--target revenue]
"""
import argparse
import numpy as np
import pandas as pd
from scipy import stats


def strength(v):
    a = abs(v)
    return "strong" if a > 0.5 else "moderate" if a > 0.3 else "weak" if a > 0.1 else "negligible"


def cramers_v(x, y):
    ct = pd.crosstab(x, y)
    chi2 = stats.chi2_contingency(ct)[0]
    n = ct.values.sum()
    r, k = ct.shape
    phi2 = chi2 / n
    phi2c = max(0, phi2 - (k - 1) * (r - 1) / (n - 1))
    rc, kc = r - (r - 1) ** 2 / (n - 1), k - (k - 1) ** 2 / (n - 1)
    return np.sqrt(phi2c / min(1e-12, min(kc - 1, rc - 1))) if min(kc, rc) > 1 else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--target", default=None)
    a = ap.parse_args()
    df = pd.read_csv(a.path)

    nums = list(df.select_dtypes(include=np.number).columns)
    cats = [c for c in df.columns if c not in nums and df[c].nunique() <= 30]

    rows = []
    for i, c1 in enumerate(nums):
        for c2 in nums[i + 1:]:
            sub = df[[c1, c2]].dropna()
            if len(sub) < 30:
                continue
            pr, pp = stats.pearsonr(sub[c1], sub[c2])
            sr, sp = stats.spearmanr(sub[c1], sub[c2])
            rows.append([f"{c1}~{c2}", "numeric", f"P={pr:+.2f}/S={sr:+.2f}", max(abs(pr), abs(sr)),
                         strength(max(abs(pr), abs(sr))), "NONLINEAR?" if abs(pr - sr) > 0.15 else ""])

    for c1 in nums:
        for c2 in cats:
            v = cramers_v(df[c2].fillna("NA"), df[c1].fillna(df[c1].median()))
            if v > 0.1:
                rows.append([f"{c2}->{c1}", "cat->num", f"V={v:.2f}", v, strength(v), ""])
    for c1, c2 in zip(cats, cats[1:]):
        pass  # categorical pairs handled below
    for i, c1 in enumerate(cats):
        for c2 in cats[i + 1:]:
            v = cramers_v(df[c1].fillna("NA"), df[c2].fillna("NA"))
            if v > 0.3:
                rows.append([f"{c1}~{c2}", "cat-cat", f"V={v:.2f}", v, strength(v), ""])

    table = pd.DataFrame(rows, columns=["pair", "type", "coef", "|effect|", "strength", "flag"]) \
        .sort_values("|effect|", ascending=False)
    print(table.head(25).to_string(index=False))

    if len(nums) >= 3:
        print("\n== VIF (multicollinearity; >5 investigate, >10 act) ==")
        from sklearn.preprocessing import StandardScaler
        from sklearn.linear_model import LinearRegression
        X = df[nums].dropna()
        Xs = StandardScaler().fit_transform(X)
        for j, c in enumerate(nums):
            others = np.delete(Xs, j, axis=1)
            r2 = LinearRegression().fit(others, Xs[:, j]).score(others, Xs[:, j])
            vif = 1 / (1 - r2) if r2 < 1 else float("inf")
            mark = " <<< ACT" if vif > 10 else (" << investigate" if vif > 5 else "")
            print(f"  {c:<30} VIF={vif:8.1f}{mark}")


if __name__ == "__main__":
    main()
