# Chart Style Settings — house standard

## Palette (colorblind-safe)
| Purpose | Hex |
|---|---|
| primary / default series | `#4a9eed` |
| highlight / the point that matters | `#e67e22` |
| negative | `#d64550` |
| positive | `#2fa360` |
| neutral context / de-emphasis | `#8a8f98` |
| categorical sets | viridis or Okabe-Ito (`#0072B2,#E69F00,#009E73,#CC79A7,#56B4E9`) |

Rules: one color = one meaning across the whole deliverable · highlight color used
ONCE per chart max · grey out context series.

## Typography & layout
| Element | Setting |
|---|---|
| title | takeaway sentence, bold, left-aligned |
| subtitle | context/unit/period, grey, small |
| font sizes | title 13–14, labels 9–10 (readable at print size) |
| gridlines | y-only, alpha ≤0.25 |
| spines | remove top & right |

## Chart-type defaults
| Type | Rule |
|---|---|
| bar | sorted desc; zero baseline; highlight one bar |
| line | direct-label ends; no legend if ≤3 lines |
| stacked bar/100% | ≤5 segments; order by size |
| scatter | alpha .5–.7; trend line only if it IS the message |
| pie | avoid; ≤3 slices with % labels if unavoidable |

## Pre-delivery checklist
- [ ] takeaway readable in 5 seconds
- [ ] zero-baseline bars
- [ ] consistent colors vs other charts in deck
- [ ] source + date on chart or footer
