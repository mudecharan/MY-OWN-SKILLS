"""generate_report.py · Markdown -> styled HTML -> PDF report generator.
Usage: python generate_report.py --input report.md --formats html,pdf [--title "Q3 Review"]
PDF strategy: weasyprint if installed; else print-ready HTML (browser Ctrl+P) fallback.
"""
import argparse
from pathlib import Path

CSS = """
body{font-family:Segoe UI,Arial,sans-serif;max-width:860px;margin:40px auto;
     color:#222;line-height:1.55;padding:0 20px}
h1{border-bottom:3px solid #4a9eed;padding-bottom:6px;color:#1a1a2e}
h2{color:#1a1a2e;border-bottom:1px solid #ddd;margin-top:32px}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:.92em}
th{background:#4a9eed;color:#fff;text-align:left;padding:7px 10px}
td{padding:6px 10px;border-bottom:1px solid #eee}
tr:nth-child(even){background:#f7f9fc}
code{background:#f0f3f7;padding:2px 5px;border-radius:3px}
blockquote{border-left:4px solid #e67e22;margin-left:0;padding-left:14px;color:#555}
.meta{color:#777;font-size:.85em}
@media print{body{margin:12mm}}
"""


def to_html(md_text: str, title: str) -> str:
    try:
        import markdown
        body = markdown.markdown(md_text, extensions=["tables", "fenced_code"])
    except ImportError:
        # minimal fallback: paragraphs, headings, bold
        import re
        body = re.sub(r"^# (.+)$", r"<h1>\1</h1>", md_text, flags=re.M)
        body = re.sub(r"^## (.+)$", r"<h2>\1</h2>", body, flags=re.M)
        body = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", body)
        body = "".join(f"<p>{l}</p>" if l.strip() and not l.startswith("<h") else l
                       for l in body.splitlines())
    return f"<!DOCTYPE html><html><head><meta charset='utf-8'><title>{title}</title>" \
           f"<style>{CSS}</style></head><body>{body}</body></html>"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="markdown source")
    ap.add_argument("--formats", default="html", help="comma list: html,pdf,md")
    ap.add_argument("--title", default="Analysis Report")
    a = ap.parse_args()

    md_path = Path(a.input)
    md_text = md_path.read_text(encoding="utf-8")
    stem = md_path.with_suffix("")
    produced = []

    for fmt in [f.strip().lower() for f in a.formats.split(",")]:
        out = Path(f"{stem}.{fmt}")
        if fmt == "md":
            out.write_text(md_text, encoding="utf-8")
        elif fmt == "html":
            out.write_text(to_html(md_text, a.title), encoding="utf-8")
        elif fmt == "pdf":
            try:
                from weasyprint import HTML
                HTML(string=to_html(md_text, a.title)).write_pdf(str(out))
            except Exception:
                fb = Path(f"{stem}_print.html")
                fb.write_text(to_html(md_text + "\n<p class='meta'>PDF engine unavailable — "
                                      "print this page to PDF (Ctrl+P).</p>", a.title),
                              encoding="utf-8")
                print(f"[fallback] weasyprint failed -> print-ready {fb} (open in browser, Ctrl+P)")
                continue
        else:
            continue
        produced.append(out)
        print(f"wrote {out}")

    print(f"\nformats done: {', '.join(str(p) for p in produced) or 'none'}")


if __name__ == "__main__":
    main()
