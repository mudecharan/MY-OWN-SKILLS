# Chart Selection Matrix

## Message-first routing
| Your takeaway sentence starts with... | Chart |
|---|---|
| "X is the biggest / ranked..." | horizontal bar, SORTED, zero baseline |
| "X is made up of..." (part-to-whole) | stacked bar; 100% bar for shares; pie ONLY ≤3 slices with labels |
| "X changed over time" | line chart; annotate events |
| "X vs Y relationship" | scatter (+ trend line); color by third variable max |
| "X distribution / spread" | histogram or box/violin per group |
| "Flow from A to B" | Sankey / funnel |
| "Geography matters" | normalized choropleth |

## Hard rules
1. Bars start at zero. Lines may zoom but label the axis clearly.
2. Position > length > angle > color in encoding accuracy.
3. One color = one meaning across the ENTIRE deliverable.
4. Direct-label lines instead of legends where possible.
5. Sorted bars, always. Alphabetical order hides the message.

## Declutter pass (in order)
- remove unnecessary gridlines → keep faint ones only for value lookup
- delete redundant legend when direct labels fit
- drop axis decimals nobody reads
- title states the TAKEAWAY ("Churn doubled in EMEA"), not the topic ("Churn by region")

## Accessibility
Okabe-Ito or viridis palettes · ≥4.5:1 contrast · readable at print size ·
never red-vs-green alone.

## Annotation = the insight
Highlight the one point that matters; add a reference line for target/last year.
The reader should get the message in 5 seconds without reading the appendix.
