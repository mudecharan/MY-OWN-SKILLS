"""ab-test-designer · design calculator + analysis with SRM/guardrail checks.
Usage:
  design:  python ab_test_tool.py design --baseline 0.10 --mde 0.02 --traffic 5000
  analyze: python ab_test_tool.py analyze --n_a 50000 --x_a 5100 --n_b 50000 --x_b 5400
"""
import argparse
import math

from scipy import stats


def design(baseline, mde, alpha=0.05, power=0.8):
    p2 = baseline + mde
    pbar = (baseline + p2) / 2
    z_a, z_b = stats.norm.ppf(1 - alpha / 2), stats.norm.ppf(power)
    n = ((z_a * math.sqrt(2 * pbar * (1 - pbar)) + z_b * math.sqrt(baseline * (1 - baseline) + p2 * (1 - p2))) ** 2) / mde ** 2
    n = math.ceil(n)
    print(f"Required n per arm: {n:,}")
    print(f"Total sample: {n*2:,}  |  relative lift: {100*mde/baseline:.1f}%")
    return n


def analyze(n_a, x_a, n_b, x_b, alpha=0.05):
    # SRM check: arms should be within ~0.5% if 50/50 intended
    expected = (n_a + n_b) / 2
    srm_dev = abs(n_a - expected) / expected
    print(f"SRM deviation: {srm_dev:.2%} {'❌ SRM FAIL — do not trust results!' if srm_dev > 0.005 else '✅'}")

    p_a, p_b = x_a / n_a, x_b / n_b
    se = math.sqrt(p_a * (1 - p_a) / n_a + p_b * (1 - p_b) / n_b)
    diff = p_b - p_a
    z = diff / se
    p_val = 2 * (1 - stats.norm.cdf(abs(z)))
    ci = (diff - 1.96 * se, diff + 1.96 * se)

    print(f"Control: {p_a:.4f}  Treatment: {p_b:.4f}")
    print(f"Absolute diff: {diff:+.4f} ({100*diff/p_a:+.1f}% relative)")
    print(f"95% CI: [{ci[0]:+.4f}, {ci[1]:+.4f}]  p={p_val:.4f}")
    verdict = "SHIP" if ci[1] > 0 and p_val < alpha else ("NO EFFECT EVIDENCE — do NOT conclude 'equal'" if p_val >= alpha else "NEGATIVE — do not ship")
    print(f"Verdict: {verdict}")
    print("Reminder: report the CI in business units; check guardrails before shipping.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("design")
    d.add_argument("--baseline", type=float, required=True)
    d.add_argument("--mde", type=float, required=True)
    d.add_argument("--traffic", type=int, default=None, help="units/day -> prints runtime")
    an = sub.add_parser("analyze")
    for f in ("n_a", "x_a", "n_b", "x_b"):
        an.add_argument(f"--{f}", type=int, required=True)
    a = ap.parse_args()
    if a.cmd == "design":
        n = design(a.baseline, a.mde)
        if a.traffic:
            print(f"Estimated runtime: {2*n/a.traffic:.1f} days at {a.traffic:,} units/day")
    else:
        analyze(a.n_a, a.x_a, a.n_b, a.x_b)
