"""bayesian-analysis-guide · Beta-Binomial A/B decisions with expected loss stopping.
Usage: python bayesian_ab.py --x_a 5100 --n_a 50000 --x_b 5400 --n_b 50000 [--threshold 0.0025]
"""
import argparse

import numpy as np
from scipy import stats


def analyze(x_a, n_a, x_b, n_b, threshold=0.0025, sims=200_000, seed=42):
    """Monte-Carlo posterior over conversion difference (Beta priors, weak)."""
    rng = np.random.default_rng(seed)
    pa = rng.beta(1 + x_a, 1 + n_a - x_a, sims)
    pb = rng.beta(1 + x_b, 1 + n_b - x_b, sims)

    p_b_beats_a = (pb > pa).mean()
    # loss if choosing an arm = how much better the OTHER arm was, on average
    expected_loss_a = np.clip(pb - pa, 0, None).mean()   # loss if we pick A
    expected_loss_b = np.clip(pa - pb, 0, None).mean()   # loss if we pick B

    print(f"P(B > A):            {p_b_beats_a:.1%}")
    print(f"E[loss | choose A]:  {expected_loss_a:.5f}")
    print(f"E[loss | choose B]:  {expected_loss_b:.5f}")
    winner = "B" if expected_loss_b < expected_loss_a else "A"
    print(f"Posterior mean lift: {100*(pb.mean()-pa.mean())/pa.mean():+.2f}%")

    if min(expected_loss_a, expected_loss_b) < threshold:
        print(f"STOP: choose {winner} — expected loss below threshold {threshold} "
              f"(safe under continuous monitoring).")
    else:
        print(f"CONTINUE collecting data (expected loss {min(expected_loss_a, expected_loss_b):.5f} "
              f"> threshold {threshold}).")

    # prior sensitivity: skeptical prior (B needs to prove itself)
    pa_s = rng.beta(1 + x_a, 1 + n_a - x_a, sims)
    pb_s = rng.beta(100 + x_b, 100 + n_b - x_b, sims)   # skeptical prior centered lower
    print(f"Skeptical-prior P(B>A): {(pb_s > pa_s).mean():.1%}  (report both views)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    for f in ("x_a", "n_a", "x_b", "n_b"):
        ap.add_argument(f"--{f}", type=int, required=True)
    ap.add_argument("--threshold", type=float, default=0.0025)
    a = ap.parse_args()
    analyze(a.x_a, a.n_a, a.x_b, a.n_b, a.threshold)
