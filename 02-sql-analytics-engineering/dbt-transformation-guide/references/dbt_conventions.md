# dbt Project Conventions

## Layout
```
models/
├── staging/            # 1:1 from sources. renames/casts/timezones ONLY.
│   └── <source>/stg_<source>__<entity>.sql + sources.yml
├── intermediate/       # business logic, joins, reusable building blocks
└── marts/              # dimensional models stakeholders query
tests/                  # singular tests = SQL returning failing rows
macros/                 # reused logic (date spine, safe_divide, pivots)
```

## Naming
- `stg_<source>__<entity>` in staging; `fct_` / `dim_` in marts.
- Past tense for events: `ordered_at`, `shipped_at`. Never `date1`.

## Layer rules
- Staging: materialized as views; never reference staging from marts twice-removed.
- Marts reference `ref()` only — never hardcode schema/table names.
- One grain per model, documented in schema.yml description.

## Testing ladder
1. Generic on every staging PK: unique, not_null.
2. accepted_values on status/enum columns.
3. relationships FK checks to dims.
4. Singular tests encoding BUSINESS rules ("cancelled orders carry no revenue").

## Safe refactor (legacy SQL → dbt) protocol
1. Wrap legacy query as-is in a model.
2. Build new model beside it.
3. Run side-by-side comparison (row count + checksums per key metric).
4. Only after parity: repoint dashboards, retire legacy.

## CI
`dbt build --select state:modified+ --defer` on PRs against a slim manifest artifact.
