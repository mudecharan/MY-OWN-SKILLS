# Feedback Mining Reference

## Pipeline order (don't skip the prep)
1. Dedupe (copy-paste spam), filter bot/boilerplate text
2. Language handling (translate or separate models per language)
3. PII scrub BEFORE anything else touches the text
4. Theme discovery → stable codebook → consistent application over time

## Codebook discipline
The codebook (~10–20 named themes) is what makes months comparable.
Unsupervised clusters DRAFT it; humans finalize names and boundaries.
Every re-code logs a version — silent codebook drift destroys trend lines.

## Sentiment model choices
| Method | Strengths | Weakness |
|---|---|---|
| Lexicon (VADER-style) | fast, no training | sarcasm/negation fragile |
| Transformer classifier | robust context | needs validation set |
Rule: hand-label ~200 comments, measure accuracy, report it. Below 80% accuracy,
sentiment numbers are decoration.

## Driver linkage (the actual point)
Theme × sentiment × structured score: which themes correlate with detractors/churn?
Report as share: "shipping delays = 31% of detractor verbatims" — that lands.

## Emerging-theme alerts
Monthly theme volumes; alert on >3σ jump. New problems announce themselves in text first.

## Close the loop
Deliver evidence packs to owning teams; track whether mentioned issues actually improve.
Feedback mining without follow-through is shelfware.
