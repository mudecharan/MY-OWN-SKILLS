"""missing-data-strategist: missingness diagnosis + imputation with validation.
Usage: python imputation_lab.py <data.csv> --cols colA,colB [--mask-test]
"""
import argparse
import numpy as np
import pandas as pd
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import SimpleImputer, IterativeImputer
from sklearn.linear_model import LogisticRegression


def diagnose(df, cols):
    print("== Missingness diagnosis ==")
    for c in cols:
        m = df[c].isna()
        pct = m.mean() * 100
        # MAR signal: does missingness in c relate to other columns?
        signals = []
        for other in df.select_dtypes(include=np.number).columns:
            if other == c or df[other].nunique() < 2:
                continue
            try:
                auc_proxy = df.groupby(m)[other].mean().diff().abs().iloc[-1]
                base = df[other].std()
                if base and auc_proxy / base > 0.3:
                    signals.append(f"{other}(mean shift {auc_proxy:.2f})")
            except Exception:
                pass
        verdict = "MCAR likely" if not signals else "MAR suspected"
        print(f"  {c}: {pct:.1f}% missing -> {verdict}; drivers: {', '.join(signals) or 'none found'}")


def mask_test(df, col):
    """Mask 10% of observed values, impute, report recovery error."""
    obs = df[col].dropna()
    rng = np.random.default_rng(42)
    idx = rng.choice(obs.index, size=max(1, int(len(obs) * 0.1)), replace=False)
    truth = df.loc[idx, col].copy()
    df.loc[idx, col] = np.nan

    if pd.api.types.is_numeric_dtype(df[col]):
        for name, imp in [("median", SimpleImputer(strategy="median")),
                          ("MICE", IterativeImputer(random_state=0))]:
            fitted = imp.fit_transform(df[[col] + [c for c in df.select_dtypes(include=np.number).columns if c != col]])
            pred = fitted[:, 0][idx]
            mae = np.abs(pred - truth).mean()
            print(f"  [{name}] MAE={mae:.3f} vs std={truth.std():.3f}")
    df.loc[idx, col] = truth


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--cols", required=True)
    ap.add_argument("--mask-test", action="store_true")
    a = ap.parse_args()
    df = pd.read_csv(a.path)
    diagnose(df, [c.strip() for c in a.cols.split(",")])
    if a.mask_test:
        print("== Imputation recovery test ==")
        for c in [c.strip() for c in a.cols.split(",")]:
            mask_test(df.copy(), c)
