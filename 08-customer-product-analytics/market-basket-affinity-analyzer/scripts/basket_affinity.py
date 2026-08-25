"""market-basket-affinity-analyzer · association rules with lift filtering + classification.
Usage: python basket_affinity.py --orders order_lines.csv --order_col order_id --item_col product
order_lines.csv: one row per item per order.
"""
import argparse
from collections import defaultdict
from itertools import combinations

import numpy as np
import pandas as pd


def mine_rules(df, order_col, item_col, min_support=0.005, min_conf=0.15, top_n=25):
    baskets = df.groupby(order_col)[item_col].apply(set)
    n = len(baskets)
    item_freq = defaultdict(int)
    pair_freq = defaultdict(int)
    for items in baskets:
        for i in items:
            item_freq[i] += 1
        for a, b in combinations(sorted(items), 2):
            pair_freq[(a, b)] += 1

    rows = []
    for (a, b), c_ab in pair_freq.items():
        support = c_ab / n
        if support < min_support:
            continue
        s_a, s_b = item_freq[a] / n, item_freq[b] / n
        conf_ab, conf_ba = support / s_a, support / s_b
        lift = support / max(1e-12, s_a * s_b)
        if lift <= 1.05 or max(conf_ab, conf_ba) < min_conf:
            continue
        # seasonal-artifact guard: affinity stable across halves of the data?
        rows.append({"A": a, "B": b, "support": round(support, 4),
                     "conf A->B": round(conf_ab, 2), "conf B->A": round(conf_ba, 2),
                     "lift": round(lift, 2)})
    rules = pd.DataFrame(rows).sort_values("lift", ascending=False)
    print(f"== Rules passing filters: {len(rules)} (top {min(top_n, len(rules))}) ==")
    print(rules.head(top_n).to_string(index=False))
    return rules, baskets


def classify_pairs(rules):
    """Complements vs substitutes need the category hierarchy; placeholder logic:
    same-category high-lift pairs are suspicious (usually complements across categories)."""
    print("\nClassification guidance:")
    print("- cross-category + lift>1.3 -> COMPLEMENT candidate (bundle/carousel)")
    print("- same-category pairs -> check substitutes: do buyers pick one OR the other?")
    print("- pairs only strong in one season/half -> SEASONAL co-occurrence, don't bundle-price on it")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--orders", required=True)
    ap.add_argument("--order-col", default="order_id")
    ap.add_argument("--item-col", default="product")
    ap.add_argument("--min-support", type=float, default=0.005)
    ap.add_argument("--min-conf", type=float, default=0.15)
    args = ap.parse_args()
    df = pd.read_csv(args.orders)
    rules, _ = mine_rules(df, args.order_col, args.item_col,
                          args.min_support, args.min_conf)
    if len(rules):
        classify_pairs(rules)


if __name__ == "__main__":
    main()
