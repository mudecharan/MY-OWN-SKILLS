"""outlier-triage: multi-method detection + sensitivity report.
Usage: python outlier_scan.py <data.csv> --cols revenue,quantity [--winsor 99]
"""
import argparse
import numpy as np
import pandas as pd


def scan(s: pd.Series) -> pd.DataFrame:
    q1, q3 = s.quantile([0.25, 0.75])
    iqr = q3 - q1
    iqr_mask = (s < q1 - 1.5 * iqr) | (s > q3 + 1.5 * iqr)
    z = (s - s.mean()) / s.std(ddof=0)
    z_mask = z.abs() > 3
    mad = np.median(np.abs(s - np.median(s))) or 1e-9
    mz = 0.6745 * (s - np.median(s)) / mad
    mad_mask = mz.abs() > 3.5
    consensus = iqr_mask & mad_mask
    return pd.DataFrame({"value": s, "iqr": iqr_mask, "z3": z_mask, "madz": mad_mask, "consensus": consensus})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--cols", required=True)
    ap.add_argument("--winsor", type=float, default=None, help="e.g. 99 to cap at P99")
    a = ap.parse_args()
    df = pd.read_csv(a.path)

    for col in [c.strip() for c in a.cols.split(",")]:
        s = pd.to_numeric(df[col], errors="coerce").dropna()
        res = scan(s)
        flagged = res[res[["iqr", "z3", "madz"]].any(axis=1)]
        print(f"\n== {col} == flagged {len(flagged):,}/{len(s):,} ({100*len(flagged)/len(s):.2f}%)")
        print(f"  consensus (IQR & MAD agree): {res.consensus.sum():,}")

        # sensitivity: metric shift if outliers excluded
        m_all, m_ex = s.mean(), s[~res.iqr].mean()
        print(f"  mean: all={m_all:,.2f}  excluding-IQR-outliers={m_ex:,.2f}  shift={100*(m_ex-m_all)/m_all:+.1f}%")

        if a.winsor:
            capped = s.clip(upper=s.quantile(a.winsor / 100))
            print(f"  winsorized at P{a.winsor}: new max={capped.max():,.2f} (was {s.max():,.2f})")

        top = flagged.reindex(flagged.value.abs().sort_values(ascending=False).index).head(10)
        print(top.assign(methods=flagged[["iqr", "z3", "madz"]].sum(axis=1)).head(10).to_string())


if __name__ == "__main__":
    main()
