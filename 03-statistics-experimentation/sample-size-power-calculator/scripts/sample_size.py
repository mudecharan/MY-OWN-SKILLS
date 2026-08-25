"""sample-size-power-calculator · n for means/proportions + simulation fallback.
Usage:
  python sample_size.py proportion --p1 0.10 --mde 0.02 [--power 0.8]
  python sample_size.py mean --sd 50 --mde 5
  python sample_size.py simulate --p1 0.10 --p2 0.12   # Monte-Carlo power check
"""
import argparse
import math

import numpy as np
from scipy import stats


def n_proportion(p1, mde, alpha=0.05, power=0.8):
    p2 = p1 + mde
    pbar = (p1 + p2) / 2
    za, zb = stats.norm.ppf(1 - alpha / 2), stats.norm.ppf(power)
    return math.ceil(((za * math.sqrt(2 * pbar * (1 - pbar)) +
                       zb * math.sqrt(p1*(1-p1) + p2*(1-p2))) ** 2) / mde ** 2)


def n_mean(sd, mde, alpha=0.05, power=0.8):
    za, zb = stats.norm.ppf(1 - alpha / 2), stats.norm.ppf(power)
    return math.ceil((2 * sd ** 2 * (za + zb) ** 2) / mde ** 2)


def simulate_power(p1, p2, n=None, alpha=0.05, sims=2000):
    """Monte-Carlo power for a two-proportion test (validates closed form).
    Uses a pooled z-test (scipy >= 1.12 removed proportions_chisquare)."""
    if n is None:
        n = n_proportion(p1, p2 - p1)
    wins = 0
    rng = np.random.default_rng(42)
    for _ in range(sims):
        xa, xb = rng.binomial(n, p1), rng.binomial(n, p2)
        pa_, pb_ = xa / n, xb / n
        se = math.sqrt(((xa + xb) / (2 * n)) * (1 - (xa + xb) / (2 * n)) * (2 / n))
        if se == 0:
            continue
        wins += abs((pb_ - pa_) / se) > stats.norm.ppf(1 - alpha / 2)
    print(f"Simulated power at n={n:,}/arm: {wins/sims:.1%} ({sims} sims)")
    return n


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="mode", required=True)

    p = sub.add_parser("proportion")
    p.add_argument("--p1", type=float, required=True)
    p.add_argument("--mde", type=float, required=True)
    p.add_argument("--alpha", type=float, default=0.05)
    p.add_argument("--power", type=float, default=0.8)

    m = sub.add_parser("mean")
    m.add_argument("--sd", type=float, required=True)
    m.add_argument("--mde", type=float, required=True)
    m.add_argument("--alpha", type=float, default=0.05)
    m.add_argument("--power", type=float, default=0.8)

    s = sub.add_parser("simulate")
    s.add_argument("--p1", type=float, required=True)
    s.add_argument("--p2", type=float, required=True)

    a = ap.parse_args()
    if a.mode == "proportion":
        n = n_proportion(a.p1, a.mde, a.alpha, a.power)
        print(f"n per arm: {n:,} | detect {a.mde:+.3f} on baseline {a.p1} "
              f"({100*a.mde/a.p1:.1f}% relative) at α={a.alpha}, power={a.power}")
        print("Attrition inflation: divide by (1 − dropout rate), e.g. 20% drop → n/0.8")
    elif a.mode == "mean":
        n = n_mean(a.sd, a.mde, a.alpha, a.power)
        print(f"n per arm: {n:,} to detect a {a.mde} shift with σ={a.sd} "
              f"(effect size d={a.mde/a.sd:.2f})")
    else:
        simulate_power(a.p1, a.p2)
