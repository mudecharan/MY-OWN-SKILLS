"""budget-variance-analyst · volume-price-mix & rate-usage decomposition.
Usage: python variance_decompose.py --qb 1000 --qa 1100 --pb 50 --pa 47
Revenue: budget vs actual units & prices. Cost mode: --mode cost with std/actual rate & qty.
"""
import argparse


def revenue_decomp(qb, qa, pb, pa, mix_base=None):
    vol = (qa - qb) * pb
    price = qa * (pa - pb)
    return {"volume": vol, "price": price,
            "total": (qa * pa) - (qb * pb)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qb", type=float, required=True, help="budget units")
    ap.add_argument("--qa", type=float, required=True, help="actual units")
    ap.add_argument("--pb", type=float, required=True, help="budget price/rate")
    ap.add_argument("--pa", type=float, required=True, help="actual price/rate")
    args = ap.parse_args()

    d = revenue_decomp(args.qb, args.qa, args.pb, args.pa)
    total = d["total"]
    print(f"Total variance: {total:+,.0f}")
    print(f"  Volume effect: ({args.qa:,.0f}-{args.qb:,.0f}) x {args.pb} = {d['volume']:+,.0f}")
    print(f"  Price  effect: {args.qa:,.0f} x ({args.pa}-{args.pb}) = {d['price']:+,.0f}")

    # mix note for multi-product: residual when decomposing product-by-product
    print("\nMulti-product: run per product; MIX = sum of per-product totals - aggregate "
          "volume+price. Mix shifts toward cheaper items can hide inside 'on-budget' revenue.")
    print("Cost variance: Rate = actual_qty x (rate_a - rate_b); "
          "Usage = (qty_a - qty_b) x rate_b.")
    print("\nCommentary checklist per material item: what / why / so-what / action — "
          "'timing' needs a stated reversal date.")


if __name__ == "__main__":
    main()
