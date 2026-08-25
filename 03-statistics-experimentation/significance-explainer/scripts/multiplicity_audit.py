"""significance-explainer · multiple-comparison correction + robustness trio.
Usage: python significance_audit.py --pvals 0.001,0.03,0.04,0.20,0.44 [--method holm|bh]
"""
import argparse

import numpy as np
from scipy import stats


def holm(p):
    order = np.argsort(p)
    m = len(p)
    adj = np.empty(m)
    running = 0
    for rank, idx in enumerate(order):
        val = (m - rank) * p[idx]
        running = max(running, val)
        adj[idx] = min(1, running)
    return adj


def benjamini_hochberg(p):
    p = np.asarray(p)
    m = len(p)
    order = np.argsort(p)
    ranked = p[order] * m / (np.arange(m) + 1)
    adjusted = np.minimum.accumulate(ranked[::-1])[::-1]
    out = np.empty(m)
    out[order] = np.clip(adjusted, 0, 1)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pvals", required=True, help="comma-separated raw p-values")
    ap.add_argument("--method", choices=["holm", "bh"], default="holm")
    a = ap.parse_args()
    p = np.array([float(x) for x in a.pvals.split(",")])

    adj = holm(p) if a.method == "holm" else benjamini_hochberg(p)

    print(f"{'raw p':>10} {'adjusted':>10}  significant@0.05   interpretation")
    for raw, ad in zip(p, adj):
        sig = "YES" if ad < 0.05 else "no"
        interp = ("evidence of effect — report estimate + CI" if ad < 0.05
                  else "no evidence of effect (NOT proof of equality)")
        print(f"{raw:>10.4f} {ad:>10.4f}   {sig:<16}  {interp}")

    print(f"\nFamily: {len(p)} comparisons · correction: "
          f"{'Holm (family-wise)' if a.method=='holm' else 'Benjamini-Hochberg (FDR)'}")
    print("Robustness checklist for every 'significant' finding:")
    print(" [ ] survives alternative test (parametric <-> non-parametric)")
    print(" [ ] survives outlier treatment change")
    print(" [ ] not driven by one subgroup alone")


if __name__ == "__main__":
    main()
