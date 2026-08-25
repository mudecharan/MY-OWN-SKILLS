"""data-governance-privacy-guardian · PII scanner + re-identification risk heuristic.
Usage: python pii_scan.py --data dataset.csv [--sample 5000]
Flags likely PII columns by name patterns + content heuristics; classifies sensitivity tier.
"""
import argparse
import re

import numpy as np
import pandas as pd

PII_NAME = re.compile(r"email|e_mail|phone|ssn|passport|dob|birth|address|first_name|"
                      r"last_name|fullname|full_name|customer_id|user_id|ip_address|"
                      r"device_id|lat|lon|latitude|longitude|iban|credit_card|card", re.I)
EMAIL_RX = re.compile(r"^[^@\s]+@[^@\s]+\.[a-z]{2,}$", re.I)
PHONE_RX = re.compile(r"^\+?[\d\s().-]{9,15}$")


def classify(col, series: pd.Series) -> str:
    sample = series.dropna().astype(str).head(2000)
    if sample.empty:
        return "empty"
    uniq_ratio = series.nunique() / max(1, len(series))
    if EMAIL_RX.match(sample.iloc[0]) or sample.str.match(EMAIL_RX).mean() > 0.5:
        return "REGULATED-PII (email)"
    if sample.str.match(PHONE_RX).mean() > 0.5:
        return "REGULATED-PII (phone)"
    if PII_NAME.search(col):
        if uniq_ratio > 0.9:
            return "REGULATED-PII (direct identifier)"
        return "CONFIDENTIAL (quasi-identifier)"
    if uniq_ratio > 0.95 and len(sample) > 50:
        return "CONFIDENTIAL (high-cardinality — possible ID)"
    return "internal"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    args = ap.parse_args()
    df = pd.read_csv(args.data)

    print(f"{'column':<25} {'tier':<42} {'null%':>6}  action")
    for c in df.columns:
        tier = classify(c, df[c])
        nulls = 100 * df[c].isna().mean()
        action = {
            "REGULATED-PII (email)": "tokenize; exclude from analytics zone",
            "REGULATED-PII (phone)": "tokenize; exclude from analytics zone",
            "REGULATED-PII (direct identifier)": "hash/token; raw access = process accounts only",
            "CONFIDENTIAL (quasi-identifier)": "generalize (zip3, age bands) in analytics zone",
            "CONFIDENTIAL (high-cardinality — possible ID)": "review: is this an ID? mask if so",
        }.get(tier, "ok for internal analytics zone")
        print(f"{c:<25} {tier:<42} {nulls:>5.0f}%  {action}")

    # re-identification heuristic on quasi-identifier combos
    qi = [c for c in df.columns if classify(c, df[c]).startswith("CONFIDENTIAL (quasi")]
    if len(qi) >= 2:
        combos = df.groupby(qi).size()
        risky = (combos == 1).mean()
        print(f"\n⚠ Quasi-identifier combo {qi}: {risky:.0%} of combinations are UNIQUE — "
              f"high re-identification risk. Generalize before sharing.")
    print("\nUnclassified = treat as highest tier. Record classification in the catalog.")


if __name__ == "__main__":
    main()
