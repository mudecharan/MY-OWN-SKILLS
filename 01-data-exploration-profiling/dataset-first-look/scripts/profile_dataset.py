"""dataset-first-look: one-command structured profile of any tabular dataset.
Usage: python profile_dataset.py <path.csv> [--key colname] [--date-cols col1,col2]
"""
import argparse
import pandas as pd
import numpy as np


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--key", default=None, help="candidate key column")
    ap.add_argument("--date-cols", default="", help="comma-separated datetime columns")
    args = ap.parse_args()

    df = pd.read_csv(args.path) if args.path.lower().endswith(".csv") else pd.read_parquet(args.path)

    print("=" * 60)
    print("1) IDENTITY")
    print(f"rows={len(df):,}  cols={df.shape[1]}  mem={df.memory_usage(deep=True).sum()/1e6:.1f} MB")

    print("\n2) KEYS & UNIQUENESS")
    if args.key and args.key in df.columns:
        print(f"key={args.key}: dupes={df[args.key].duplicated().sum():,} nulls={df[args.key].isna().sum():,}")
    full_dupes = df.duplicated().sum()
    print(f"full-row duplicates: {full_dupes:,}")

    print("\n3) NULL MAP (top 20)")
    nulls = (df.isna().mean() * 100).sort_values(ascending=False)
    print(nulls.head(20).round(1).to_string())

    print("\n4) CARDINALITY")
    card = df.nunique().sort_values()
    for c in df.columns:
        role = "ID-like" if card[c] > 0.9 * len(df) else ("constant" if card[c] <= 1 else f"nunique={card[c]}")
        print(f"  {c:<35} {role}")

    print("\n5) TEMPORAL ENVELOPE")
    date_cols = [c.strip() for c in args.date_cols.split(",") if c.strip()]
    for c in date_cols:
        s = pd.to_datetime(df[c], errors="coerce")
        gaps = s.sort_values().diff().dt.days.value_counts().head(3)
        print(f"  {c}: {s.min()} -> {s.max()} | top day-gaps: {gaps.to_dict()}")

    print("\n6) NUMERIC SANITY (negatives where suspicious)")
    for c in df.select_dtypes(include=np.number).columns:
        neg = (df[c] < 0).sum()
        if neg:
            print(f"  WARNING {c}: {neg:,} negative values (min={df[c].min():.2f})")


if __name__ == "__main__":
    main()
