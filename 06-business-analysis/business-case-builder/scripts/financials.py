"""business-case-builder · NPV/ROI/payback + sensitivity calculator.
Usage: python financials.py --initial 120000 --annual 45000 --years 3 --rate 0.10
       python financials.py --sensitivity --initial 120000 --annual 45000 --years 3 --rate 0.10
"""
import argparse


def npv(initial, annual, years, rate, growth=0.0):
    return -initial + sum(annual * (1 + growth) ** t / (1 + rate) ** t
                          for t in range(1, years + 1))


def payback(initial, annual, years, growth=0.0):
    cum, prev = -initial, -initial
    for t in range(1, years + 1):
        cf = annual * (1 + growth) ** t
        cum += cf
        if cum >= 0 > prev:
            frac = -prev / cf
            return t - 1 + frac
        prev = cum
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--initial", type=float, required=True)
    ap.add_argument("--annual", type=float, required=True)
    ap.add_argument("--years", type=int, default=3)
    ap.add_argument("--rate", type=float, default=0.10)
    ap.add_argument("--growth", type=float, default=0.0)
    ap.add_argument("--sensitivity", action="store_true")
    a = ap.parse_args()

    v = npv(a.initial, a.annual, a.years, a.rate, a.growth)
    pb = payback(a.initial, a.annual, a.years, a.growth)
    roi = a.annual * a.years / a.initial
    print(f"NPV @{a.rate:.0%}: ${v:,.0f}  |  Payback: {pb:.1f} yrs" if pb else
          f"NPV @{a.rate:.0%}: ${v:,.0f}  |  Payback: >{a.years} yrs")
    print(f"Simple ROI over {a.years}y: {roi:.0%}")

    if a.sensitivity:
        print("\nSensitivity: NPV across benefit-realization × cost-overrun")
        print(f"{'':>14}" + "".join(f"{'cost+'+str(o):>12}" for o in (0, 25, 50)))
        for b in (1.0, 0.75, 0.5):
            row = f"{'benefit×'+str(b):<14}"
            for o in (0, 0.25, 0.5):
                val = npv(a.initial * (1 + o), a.annual * b, a.years, a.rate, a.growth)
                row += f"{val:>12,.0f}"
            print(row)
        print("If NPV < 0 in any plausible cell → state the case as conditional.")


if __name__ == "__main__":
    main()
