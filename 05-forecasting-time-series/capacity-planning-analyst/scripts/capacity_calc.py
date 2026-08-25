"""capacity-planning-analyst · FTE requirement + scenario grid + Erlang C (if available).
Usage: python capacity_calc.py --volume 12000 --aht_min 8 --shift_min 420 --shrinkage 0.30 --occupancy 0.80
"""
import argparse
import math


def fte_required(volume, aht_min, shift_min, shrinkage, occupancy):
    work_minutes = volume * aht_min
    productive = shift_min * (1 - shrinkage) * occupancy
    return work_minutes / productive


def erlang_c_required_agents(arrivals_per_hour, aht_sec, sl_target=0.8, ta_sec=20, max_agents=200):
    try:
        from pyworkforce.queuing import ErlangC
        res = ErlangC(transactions=arrivals_per_hour, aht=aht_sec,
                      interval=3600, asa=ta_sec, target=sl_target).required_positions()
        return res
    except ImportError:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--volume", type=float, required=True, help="workload units per day")
    ap.add_argument("--aht-min", type=float, required=True, help="handle time incl. wrap-up")
    ap.add_argument("--shift-min", type=float, default=420)
    ap.add_argument("--shrinkage", type=float, default=0.30)
    ap.add_argument("--occupancy", type=float, default=0.80)
    ap.add_argument("--attrition", type=float, default=0.15, help="annual attrition -> extra headcount")
    args = ap.parse_args()

    core = fte_required(args.volume, args.aht_min, args.shift_min,
                        args.shrinkage, args.occupancy)
    with_attrition = core / (1 - args.attrition)

    print(f"Work minutes/day:        {args.volume * args.aht_min:>12,.0f}")
    print(f"Productive min per FTE:  {args.shift_min*(1-args.shrinkage)*args.occupancy:>12,.1f}")
    print(f"FTE required (steady):   {core:>12.1f}")
    print(f"Heads to hire/hold (+{args.attrition:.0%} attrition): {with_attrition:>8.1f}")
    if args.occupancy > 0.85:
        print("⚠ occupancy >85% — queue growth becomes non-linear; SLA risk")

    # scenario grid
    print("\n== Scenario grid (FTE steady-state) ==")
    print(f"{'demand':<10} {'occ .75':>9} {'occ .80':>9} {'occ .85':>9}")
    for dem in (0.8, 1.0, 1.2):
        row = [fte_required(args.volume*dem, args.aht_min, args.shift_min,
                            args.shrinkage, occ) for occ in (0.75, 0.80, 0.85)]
        print(f"{f'{dem:+.0%}':<10} " + " ".join(f"{v:>9.1f}" for v in row))

    # lever analysis
    for name, factor in [("self-service deflection −15% volume", 0.85),
                         ("AHT reduction −10%", None)]:
        v = args.volume * factor if factor else None
        aht = args.aht_min * 0.9 if not factor else args.aht_min
        fte = fte_required(v or args.volume, aht, args.shift_min, args.shrinkage, args.occupancy)
        print(f"Lever '{name}': saves {core - fte:.1f} FTE-equivalents")


if __name__ == "__main__":
    main()
