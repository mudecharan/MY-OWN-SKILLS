"""market-swot-competitor-analyst · TAM/SAM/SOM sizing calculator (top-down × bottom-up).
Usage: python market_sizing.py --tam_topdown 2.4e9 --segment_share 0.18 --price 12000
                               --reachable_accounts 4000 --target_share 0.05
"""
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tam-topdown", type=float, required=True, help="industry report $ total")
    ap.add_argument("--segment-share", type=float, required=True,
                    help="our segment's share of that industry (0-1)")
    ap.add_argument("--price", type=float, required=True, help="ACV / unit price")
    ap.add_argument("--accounts", type=float, default=None,
                    help="total accounts in segment (bottom-up)")
    ap.add_argument("--reachable-accounts", type=float, default=None)
    ap.add_argument("--target-share", type=float, default=0.05, help="SOM share assumption")
    a = ap.parse_args()

    tam_td = a.tam_topdown
    sam_td = tam_td * a.segment_share

    if a.accounts:
        tam_bu = a.accounts * a.price
        print(f"TAM: top-down ${tam_td:,.0f} vs bottom-up ${tam_bu:,.0f} "
              f"(divergence {abs(tam_bu-tam_td)/tam_td:.0%} — >2x means fuzzy segment definition!)")
    sam_bu = (a.reachable_accounts or 0) * a.price
    som = (sam_bu or sam_td) * a.target_share

    print(f"SAM: top-down ${sam_td:,.0f}" +
          (f" vs bottom-up (reachable×price) ${sam_bu:,.0f}" if sam_bu else ""))
    print(f"SOM @ {a.target_share:.0%} target share: ${som:,.0f}")
    print("\nRule: reconcile both methods; SOM must trace to YOUR funnel capacity, not ambition.")
    print("Funnel sanity: SOM / ACV = accounts needed → check against lead volume × conversion.")


if __name__ == "__main__":
    main()
