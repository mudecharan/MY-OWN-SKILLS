"""clv-ltv-modeler · cohort CLV curves + BG/NBD + Gamma-Gamma forward value (lifetimes lib).
Usage: python clv_model.py --tx transactions.csv --customer_col id --date_col date --amount_col amount
Falls back to empirical cohort curves if lifetimes is not installed.
"""
import argparse

import numpy as np
import pandas as pd


def cohort_curves(tx, cust, date, amt, months=12):
    tx = tx.copy()
    tx[date] = pd.to_datetime(tx[date])
    tx["cohort"] = tx.groupby(cust)[date].transform("min").dt.to_period("M")
    tx["month_idx"] = ((tx[date].dt.to_period("M") - tx["cohort"]).apply(lambda x: x.n))
    curves = (tx[tx.month_idx < months]
              .groupby(["cohort", "month_idx"])[amt].sum()
              .groupby("cohort").cumsum().unstack(0))
    print("== Cumulative margin per customer by monthly cohort (first %d months) ==" % months)
    n_cust = tx.groupby("cohort")[cust].nunique()
    print((curves.div(n_cust, axis=1)).round(1).fillna("").to_string())
    return curves


def btyd_forward_value(tx, cust, date, amt):
    """BG/NBD + Gamma-Gamma on customers with >=1 repeat purchase."""
    try:
        from lifetimes import BetaGeoFitter, GammaGammaFitter
        from lifetimes.utils import summary_data_from_transaction_data
    except ImportError:
        print("\n[lifetimes not installed — pip install lifetimes for BTYD models]")
        return None
    summary = summary_data_from_transaction_data(tx, cust, date, monetary_value_col=amt)
    repeat = summary[summary.frequency > 0]

    bgf = BetaGeoFitter(penalizer_coef=0.01).fit(repeat["frequency"], repeat["recency"], repeat["T"])
    ggf = GammaGammaFitter(penalizer_coef=0.01).fit(repeat["frequency"], repeat["monetary_value"])

    summary["clv_12m"] = ggf.customer_lifetime_value(
        bgf, summary["frequency"], summary["recency"],
        summary["T"], summary["monetary_value"], time=12, freq="D")
    print("\n== Forward 12-month value (BG/NBD + Gamma-Gamma, repeat buyers) ==")
    print(summary["clv_12m"].describe(percentiles=[.25, .5, .75, .9]).round(0).to_string())
    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tx", required=True)
    ap.add_argument("--customer-col", default="customer_id")
    ap.add_argument("--date-col", default="date")
    ap.add_argument("--amount-col", default="amount")
    a = ap.parse_args()
    tx = pd.read_csv(a.tx)
    cohort_curves(tx, a.customer_col, a.date_col, a.amount_col)
    btyd_forward_value(tx, a.customer_col, a.date_col, a.amount_col)
    print("\nDecision hooks: LTV:CAC by channel (kill below threshold) · "
          "early-life indicators of high CLV · feed segments into segmentation-builder")
