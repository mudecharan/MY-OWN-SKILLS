# Dashboard Wireframe Spec — <dashboard name>

## 1. Audience & job (before any layout)
| Question | Answer |
|---|---|
| Who opens this, when? | |
| THE one question it answers | |
| Decision/action taken from the answer | |
| If none → recommend a REPORT instead | |

## 2. Layout wireframe (F-pattern; top-left = most important)
```
+--------------------------------------------------------------+
| HEADLINE KPIs (3-5 max): value + vs-target delta + sparkline |
+---------------------------+----------------------------------+
| PRIMARY DRIVER VISUAL     | BREAKDOWN / SEGMENT VIEW          |
| (the "why" behind KPIs)   |                                   |
+---------------------------+----------------------------------+
| DETAIL TABLE (or linked out) — last, collapsible             |
+--------------------------------------------------------------+
```

## 3. Visual inventory
| Position | Visual | Metric definitions (link to catalog) | Interactions |
|---|---|---|---|

## 4. Interaction design
- Date default = business cycle (e.g., current month)
- Cross-filtering only where a real question exists
- No more than __ dropdowns

## 5. Performance & trust
- [ ] aggregate tables under visuals (no live fact-table queries)
- [ ] page load <5s target
- [ ] every tile shows refresh timestamp + source
- [ ] metric definition link on-page

## 6. Launch & prune plan
Usage review after 30 days · remove unused tiles · quarterly maintenance owner: ____
