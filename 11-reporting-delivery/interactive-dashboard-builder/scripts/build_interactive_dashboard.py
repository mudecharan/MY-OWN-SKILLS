"""build_interactive_dashboard.py · single-file interactive HTML dashboard (Plotly).
Usage: python build_interactive_dashboard.py --config dashboard_config.json
Config format:
{
  "title": "Sales Explorer",
  "filters": ["region", "channel"],
  "kpis": [{"label": "Revenue", "column": "revenue", "agg": "sum"}],
  "charts": [
    {"type": "bar", "x": "region", "y": "revenue", "agg": "sum", "title": "Revenue by region"},
    {"type": "line", "x": "month", "y": "revenue", "agg": "sum", "color": "channel"}
  ]
}
Data: --data data.csv (one flat table; filters are its columns).
"""
import argparse
import json

import pandas as pd


def agg_expr(df, spec):
    col, fn = spec["y"], spec.get("agg", "sum")
    if fn == "count":
        return df.groupby(spec["x"]).size().rename(col or "count")
    g = df.groupby([spec["x"]] + ([spec["color"]] if spec.get("color") else []))[col]
    return getattr(g, fn)()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", default="dashboard.html")
    a = ap.parse_args()

    df = pd.read_csv(a.data)
    cfg = json.loads(open(a.config, encoding="utf-8").read())

    import plotly.express as px
    import plotly.graph_objects as go

    kpi_rows = []
    for k in cfg.get("kpis", []):
        val = getattr(df[k["column"]], k.get("agg", "sum"))()
        kpi_rows.append(f"<div class='kpi'><div class='kpi-l'>{k['label']}</div>"
                        f"<div class='kpi-v'>{val:,.0f}</div></div>")

    figs = []
    for spec in cfg.get("charts", []):
        t = spec["type"]
        d = agg_expr(df, spec).reset_index()
        ttl = spec.get("title", "Chart")
        if t == "bar":
            fig = px.bar(d, x=spec["x"], y=d.columns[-1],
                         color=spec.get("color"), title=ttl)
        elif t == "line":
            fig = px.line(d, x=spec["x"], y=d.columns[-1],
                          color=spec.get("color"), title=ttl, markers=True)
        elif t == "scatter":
            fig = px.scatter(df, x=spec["x"], y=spec["y"],
                             color=spec.get("color"), title=ttl)
        else:
            continue
        fig.update_layout(template="plotly_white",
                          margin=dict(l=30, r=30, t=50, b=30), height=340)
        figs.append(fig.to_html(full_html=False, include_plotlyjs=False))

    filter_html = ""
    for f in cfg.get("filters", []):
        opts = sorted(df[f].dropna().unique())
        opts_html = "".join(f"<option value='{o}'>{o}</option>" for o in opts)
        filter_html += (f"<label>{f}<select id='f_{f}' multiple size={min(4,len(opts))}>"
                        f"{opts_html}</select></label>")

    html = f"""<!DOCTYPE html><html><head><meta charset='utf-8'>
<title>{cfg['title']}</title>
<script src='https://cdn.plot.ly/plotly-2.32.0.min.js'></script>
<style>
body{{font-family:Segoe UI,Arial;max-width:1100px;margin:24px auto;color:#222;padding:0 16px}}
h1{{border-bottom:3px solid #4a9eed}}
.kpis{{display:flex;gap:16px;margin:14px 0}}
.kpi{{flex:1;background:#f0f5fb;border-radius:8px;padding:12px 16px}}
.kpi-l{{font-size:.8em;color:#666}} .kpi-v{{font-size:1.7em;font-weight:700;color:#1a1a2e}}
.filters{{margin:10px 0;display:flex;gap:14px}} select{{min-width:130px}}
.meta{{color:#777;font-size:.85em}}
</style></head><body>
<h1>{cfg['title']}</h1>
<div class='meta'>Data through {df.iloc[:, -1].max() if len(df) else 'n/a'} · self-serve exploration</div>
<div class='filters'>{filter_html}</div>
<div class='kpis'>{''.join(kpi_rows)}</div>
{''.join(figs)}
<p class='meta'>Filters are illustrative in static mode — regenerate with filtered data
or wire callbacks for live filtering.</p>
</body></html>"""

    open(a.out, "w", encoding="utf-8").write(html)
    print(f"dashboard -> {a.out} ({len(figs)} charts, {len(cfg.get('filters', []))} filters)")
    print("Open in a browser. Run the 5-second test before sharing.")


if __name__ == "__main__":
    main()
