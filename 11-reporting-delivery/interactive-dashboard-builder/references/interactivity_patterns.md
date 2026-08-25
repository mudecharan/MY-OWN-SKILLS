# Interactivity Patterns Reference

## Match interaction to the real question
| Stakeholder behavior | Right interaction |
|---|---|
| "How does this look for MY region?" | dropdown/checkbox filters |
| "What drove the number?" | drill-down: KPI → driver chart → detail table |
| "How did we get here vs last year?" | time-range selector + comparison toggle |
| "Which items are outliers?" | hover details + click-to-filter |
| "Can I have the raw data?" | download button (controlled export) |

## Rules
1. Every filter must serve a recurring question — decorative filters add confusion.
2. Filters should cascade logically (region → store, year → month).
3. Default state = the most common question (usually latest full period).
4. Cap visible options (~20); group into "All" + top-N + "Other".
5. Show applied filters on every exported view.

## Single-file HTML dashboards (this skill's default)
- Plotly figures embedded; shareable via email/drive; works offline (except CDN script).
- For live cross-filtering in one file: embed data as JSON + small JS callback, or
  regenerate per audience. For heavy self-serve needs, graduate to a BI tool instead.

## Performance budget
- Pre-aggregate under every visual (<10M rows scanned per refresh).
- <5s first paint or adoption dies.
- Limit to ≤12 visuals per page.

## Handover checklist
- [ ] 5-second test passed with an actual stakeholder
- [ ] refresh instructions + data owner documented on-page
- [ ] metric definitions linked
