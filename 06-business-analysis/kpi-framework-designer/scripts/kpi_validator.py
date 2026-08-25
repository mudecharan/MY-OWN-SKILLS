"""kpi-framework-designer · definition completeness validator.
Usage: python kpi_validator.py --catalog kpi_catalog.csv
Catalog columns: kpi, formula, grain, source, refresh, owner, exclusions, target
"""
import argparse
import pandas as pd

REQUIRED = ["kpi", "formula", "grain", "source", "refresh", "owner", "exclusions", "target"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", required=True)
    a = ap.parse_args()
    df = pd.read_csv(a.catalog)

    missing_cols = [c for c in REQUIRED if c not in df.columns]
    if missing_cols:
        raise SystemExit(f"catalog missing columns: {missing_cols}")

    problems = []
    for _, row in df.iterrows():
        gaps = [c for c in REQUIRED if pd.isna(row[c]) or str(row[c]).strip() in ("", "TODO")]
        if gaps:
            problems.append((row["kpi"], gaps))
        if pd.isna(row["owner"]) or "@" not in str(row.get("owner", "")):
            # owner must be a person; heuristic flag
            problems.append((row["kpi"], ["owner is not a named person?"]))

    if problems:
        print("INCOMPLETE DEFINITIONS (blocks sign-off):")
        for kpi, gaps in problems:
            print(f"  {kpi}: {', '.join(gaps)}")
    else:
        print("All KPI definitions complete: formula, grain, source, refresh, "
              "named owner, exclusions, target. ✓")
    print(f"\n{len(df)} KPIs reviewed. Rule: no KPI enters a dashboard without full definition.")


if __name__ == "__main__":
    main()
