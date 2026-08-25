"""financial-statement-analyzer · ratio calculator with DuPont + red flags.
Usage: python ratios.py --fin financials.csv --years 2021 2022 2023
financials.csv columns (rows=metrics, cols=years): revenue, cogs, net_income,
total_assets, equity, current_assets, current_liabilities, inventory,
receivables, payables, ebit, interest_expense, ocf.
"""
import argparse

import pandas as pd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fin", required=True)
    ap.add_argument("--years", nargs="+", required=True)
    a = ap.parse_args()
    f = pd.read_csv(a.fin).set_index("metric")
    years = [str(y) for y in a.years]
    rows = []

    def g(m, y):
        try:
            return float(f.loc[m, y])
        except Exception:
            return None

    for y in years:
        rev, cogs, ni = g("revenue", y), g("cogs", y), g("net_income", y)
        ta, eq = g("total_assets", y), g("equity", y)
        ca, cl = g("current_assets", y), g("current_liabilities", y)
        inv, rec, pay = g("inventory", y), g("receivables", y), g("payables", y)
        ebit, ie, ocf = g("ebit", y), g("interest_expense", y), g("ocf", y)

        margin = ni / rev if rev else None
        turnover = rev / ta if ta else None
        leverage = ta / eq if eq else None
        roe = margin * turnover * leverage if all([margin, turnover, leverage]) else None
        dso = 365 * rec / rev if rec and rev else None
        dio = 365 * inv / cogs if inv and cogs else None
        dpo = 365 * pay / cogs if pay and cogs else None
        ccc = sum(v for v in [dso, dio, -(dpo or 0)] if v is not None) or None

        rows.append({
            "year": y,
            "gross_margin%": round(100 * (rev - cogs) / rev, 1) if rev and cogs else None,
            "net_margin%": round(100 * margin, 1) if margin else None,
            "asset_turn": round(turnover, 2) if turnover else None,
            "leverage": round(leverage, 2) if leverage else None,
            "ROE%": round(100 * roe, 1) if roe else None,
            "current_ratio": round(ca / cl, 2) if ca and cl else None,
            "interest_cover": round(ebit / ie, 1) if ebit and ie else None,
            "DSO": round(dso) if dso else None,
            "DIO": round(dio) if dio else None,
            "DPO": round(dpo) if dpo else None,
            "CCC": round(ccc) if ccc is not None else None,
            "OCF/NI": round(ocf / ni, 2) if ocf and ni else None,
        })

    out = pd.DataFrame(rows)
    print(out.to_string(index=False))
    print("\nRed-flag probes:")
    for i in range(1, len(years)):
        prev, cur = out.iloc[i-1], out.iloc[i]
        flags = []
        if cur["DSO"] and prev["DSO"] and cur["DSO"] - prev["DSO"] > 10:
            flags.append("DSO jump ≥10 days (collections/channel stuffing?)")
        if cur["OCF/NI"] and cur["OCF/NI"] < 0.8:
            flags.append("OCF < 80% of net income (accrual-heavy earnings)")
        if cur["gross_margin%"] and prev["gross_margin%"] and \
                cur["gross_margin%"] < prev["gross_margin%"]:
            flags.append("gross margin declining — check discounting/cost inflation")
        if flags:
            print(f"  {cur['year']}: " + "; ".join(flags))


if __name__ == "__main__":
    main()
