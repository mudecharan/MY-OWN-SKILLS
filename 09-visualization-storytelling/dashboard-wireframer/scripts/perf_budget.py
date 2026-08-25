"""dashboard-wireframer · performance budget checker for planned dashboards.
Usage: python perf_budget.py --manifest dashboard_manifest.csv
manifest columns: tile, visual_type, source_table, rows_scanned, refresh_per_day
Budgets: <5s page load ≈ sum of scan cost; high-cardinality visual types flagged.
"""
import argparse

import pandas as pd

HEAVY_VISUALS = {"scatter", "map", "table", "treemap"}
MAX_SCAN_ROWS_PER_TILE = 10_000_000      # 10M rows per tile per refresh = redesign
MAX_TILES = 12
REFRESH_BUDGET_PER_DAY = 200             # total scheduled refreshes across tiles


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    args = ap.parse_args()
    df = pd.read_csv(args.manifest)
    df["rows_scanned"] = pd.to_numeric(df["rows_scanned"], errors="coerce")
    df["refresh_per_day"] = pd.to_numeric(df["refresh_per_day"], errors="coerce").fillna(1)

    print(f"tiles: {len(df)} (budget <= {MAX_TILES}) "
          f"{'!! TOO MANY - split pages or prune' if len(df) > MAX_TILES else 'OK'}")

    df["scan_flag"] = df["rows_scanned"] > MAX_SCAN_ROWS_PER_TILE
    df["heavy"] = df["visual_type"].str.lower().isin(HEAVY_VISUALS)

    print("\nPer-tile check:")
    for _, r in df.iterrows():
        notes = []
        if r["scan_flag"]:
            notes.append("!! scans >10M rows - aggregate table needed")
        if r["heavy"]:
            notes.append("heavy visual type - cap cardinality / pre-aggregate")
        print(f"  {r['tile']:<30} rows={r['rows_scanned']:>12,.0f}  {'; '.join(notes) or 'OK'}")

    total_refreshes = int(df["refresh_per_day"].sum())
    print(f"\ntotal scheduled refreshes/day: {total_refreshes} "
          f"(budget {REFRESH_BUDGET_PER_DAY}) "
          f"{'!! refresh storm - event-based or shared cache' if total_refreshes > REFRESH_BUDGET_PER_DAY else 'OK'}")

    offenders = df[df[["scan_flag", "heavy"]].any(axis=1)]
    if len(offenders):
        est = (offenders["rows_scanned"].sum() * offenders["refresh_per_day"].sum())
        print(f"estimated daily scanned rows from flagged tiles: {est:,.0f} — "
              f"these drive both load time and warehouse cost.")


if __name__ == "__main__":
    main()
