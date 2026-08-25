"""dbt-transformation-guide · project scaffold generator.
Usage: python dbt_scaffold.py --name analytics --sources raw,salesforce
Creates folder layout, sources.yml skeleton, naming-convention README.
"""
import argparse
from pathlib import Path

README = """# Conventions
- staging: stg_<source>__<entity>.sql — renames/casts ONLY, no business logic
- intermediate: reusable business logic blocks
- marts: fct_ / dim_ models stakeholders query; one grain each, documented in schema.yml
- every staging PK gets unique + not_null tests before merge
"""

SOURCES_YML = """version: 2

sources:
{blocks}
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", default="analytics")
    ap.add_argument("--sources", default="raw", help="comma list of source systems")
    a = ap.parse_args()
    root = Path(a.name)

    for layer in ("staging", "intermediate", "marts"):
        (root / "models" / layer).mkdir(parents=True, exist_ok=True)
        if layer == "staging":
            for src in [s.strip() for s in a.sources.split(",")]:
                (root / "models" / "staging" / src).mkdir(exist_ok=True)
    (root / "tests").mkdir(exist_ok=True)
    (root / "macros").mkdir(exist_ok=True)
    (root / "README.md").write_text(README)

    blocks = []
    for src in [s.strip() for s in a.sources.split(",")]:
        blocks.append(f"""  - name: {src}
    database: <warehouse_db>
    schema: {src}_raw
    tables:
      - name: example_table
        description: "TODO: document grain + columns"
""")
    (root / "models" / "staging" / "sources.yml").write_text(SOURCES_YML.format(blocks="\n".join(blocks)))
    print(f"scaffolded {root}/ — next: fill sources.yml, add stg models with tests")

if __name__ == "__main__":
    main()
