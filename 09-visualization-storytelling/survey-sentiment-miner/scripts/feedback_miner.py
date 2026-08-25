"""survey-sentiment-miner · theme clustering + lexicon sentiment + theme-score linkage.
Usage: python feedback_miner.py --text comments.csv --col comment [--scores scores.csv --score_col nps]
comments.csv: one row per verbatim. scores.csv optional: respondent-level score for driver linkage.
"""
import argparse
import re
from collections import Counter

import numpy as np
import pandas as pd

POS = {"good": 1, "great": 1, "love": 1, "excellent": 1.5, "easy": 1, "fast": 1,
       "helpful": 1, "perfect": 1.5, "best": 1}
NEG = {"bad": -1, "slow": -1, "hate": -1, "terrible": -1.5, "difficult": -1,
       "expensive": -.8, "broken": -1.2, "worst": -1.5, "confusing": -1,
       "late": -1, "delay": -1, "delayed": -1}


def clean(t: str) -> str:
    t = re.sub(r"http\S+", "", str(t).lower())
    return re.sub(r"[^a-z0-9' ]", " ", t)


def lexicon_sentiment(t: str) -> float:
    toks = clean(t).split()
    s, neg = 0.0, False
    for w in toks:
        if w in ("not", "never", "no"):
            neg = not neg
            continue
        v = POS.get(w, NEG.get(w, 0))
        s += (-v if (neg and v) else v)
        if w not in ("not", "never", "no"):
            neg = False
    return s


def themes(texts, n_themes=8):
    """Co-occurrence keyword clusters as a lightweight codebook draft."""
    vecs = []
    from collections import defaultdict
    kw = Counter()
    for t in texts:
        toks = [w for w in clean(t).split() if len(w) > 3 and w not in
                ("this", "that", "with", "have", "very", "just", "your", "from", "they")]
        kw.update(set(toks))          # document frequency
    top = [w for w, _ in kw.most_common(60)]
    # group keywords by co-occurrence within comments
    cooc = defaultdict(Counter)
    sets_ = [set(clean(t).split()) & set(top) for t in texts]
    for s in sets_:
        for a in s:
            for b in s:
                if a < b:
                    cooc[a][b] += 1
    used, themes_out = set(), []
    for a, _ in kw.most_common(60):
        if a in used:
            continue
        partners = [b for b, c in cooc[a].most_common(4) if c >= 3 and b not in used]
        group = [a] + partners
        used.update(group)
        themes_out.append(group)
        if len(themes_out) >= n_themes:
            break
    return themes_out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", required=True)
    ap.add_argument("--col", default="comment")
    ap.add_argument("--scores", default=None)
    ap.add_argument("--score-col", default="nps")
    args = ap.parse_args()

    df = pd.read_csv(args.text)
    df["sent"] = df[args.col].map(lexicon_sentiment)
    print(f"n={len(df)} · mean sentiment={df['sent'].mean():+.2f} · "
          f"{100*(df['sent']<-0.3).mean():.0f}% clearly negative")

    th = themes(df[args.col])
    print("\n== Draft theme groups (refine into a stable codebook with the team) ==")
    for i, grp in enumerate(th):
        mask = df[args.col].str.contains("|".join(grp), case=False, na=False)
        print(f"  T{i+1}: {' / '.join(grp[:6]):<50} n={mask.sum():>5}  "
              f"avg_sent={df.loc[mask,'sent'].mean():+.2f}")

    if args.scores:
        sc = pd.read_csv(args.scores)
        m = df.merge(sc.reset_index(), left_index=True, right_on="index")
        detractors = m[m[args.score_col] <= 6]
        print(f"\n== Detractor themes ({len(detractors)} comments) ==")
        for i, grp in enumerate(th):
            mask = detractors[args.col].str.contains("|".join(grp), case=False, na=False)
            share = 100 * mask.sum() / max(1, len(detractors))
            if share > 5:
                print(f"  T{i+1} {'/'.join(grp[:3]):<30} {share:.0f}% of detractor comments")
    print("\nValidate sentiment on ~200 hand-labeled samples before trusting it.")


if __name__ == "__main__":
    main()
