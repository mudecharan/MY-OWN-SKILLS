"""pricing-optimization-analyst · elasticity → profit-maximizing price move scenarios.
Usage: python elasticity_scenarios.py --price 100 --cost 60 --qty 10000 --elasticity -1.8 [--pct 5]
"""
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--price", type=float, required=True)
    ap.add_argument("--cost", type=float, required=True)
    ap.add_argument("--qty", type=float, required=True)
    ap.add_argument("--elasticity", type=float, required=True, help="negative, e.g. -1.8")
    ap.add_argument("--pct", type=float, default=5.0, help="scenario price moves plus/minus N percent")
    args = ap.parse_args()

    e = abs(args.elasticity)
    base_margin = (args.price - args.cost) * args.qty

    print(f"Baseline: price={args.price} cost={args.cost} qty={args.qty:,.0f} "
          f"margin=${base_margin:,.0f} | margin%={100*(args.price-args.cost)/args.price:.0f}%")
    print(f"Elasticity {args.elasticity} -> {'ELASTIC (>1): cutting price can grow profit' if e > 1 else 'INELASTIC (<1): raise price toward profit-max'}")

    # Lerner / inverse-elasticity optimum markup: P* = e/(e+1) x cost for |e|>1
    if e > 1:
        p_star = e / (e - 1) * args.cost
        print(f"Profit-maximizing price ~ e/(e-1)*cost = ${p_star:,.2f} "
              f"(current ${args.price}) - sanity check vs strategy constraints.")

    print("\n== Scenario grid ==")
    print(f"{'move':>7} {'new price':>10} {'est. qty':>12} {'margin $':>14} {'vs base':>12}")
    for pct in (-args.pct, 0, args.pct):
        new_p = args.price * (1 + pct / 100)
        new_q = args.qty * (1 + args.elasticity * pct / 100)
        m = (new_p - args.cost) * new_q
        print(f"{pct:>+6.0f}% {new_p:>10,.2f} {new_q:>12,.0f} {m:>14,.0f} "
              f"{m-base_margin:>+12,.0f}")

    print("\nCaveats: constant elasticity assumption; validate with geo/cohort split test "
          "before rollout; watch competitor response.")


if __name__ == "__main__":
    main()
