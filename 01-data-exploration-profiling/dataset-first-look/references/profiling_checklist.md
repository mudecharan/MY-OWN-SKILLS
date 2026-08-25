# Profiling Checklist (work top-to-bottom before declaring a dataset understood)

## Grain
- [ ] One sentence written: "One row = one ___"
- [ ] Grain validated against duplicate counts at declared key(s)

## Identity & keys
- [ ] Row count matches source claim (extract logs, row counts from owner)
- [ ] Natural key candidate tested: unique? any NULLs in key?
- [ ] Surrogate key gaps checked (missing IDs suggest deleted rows upstream)

## Missingness
- [ ] Null % computed per column; columns >5% listed for follow-up
- [ ] Pattern classified: random vs block (blocks → join/upstream failure)
- [ ] Missingness correlated across columns? (co-null matrix)

## Cardinality
- [ ] High-cardinality columns identified (IDs → exclude from aggregation checks)
- [ ] Low-cardinality columns inventoried as dimensions/flags
- [ ] Constant columns flagged as dead weight

## Time coverage
- [ ] Min/max dates recorded per datetime column
- [ ] Gaps detected (resample daily/monthly and diff)
- [ ] Timezone convention confirmed with data owner

## Value sanity
- [ ] Sign checks (negative revenue? negative age?)
- [ ] Impossible values (dates in future beyond extract date)
- [ ] Mixed types inside text columns (numbers stored as strings)
- [ ] Encoding artifacts (Ã©, â€™) indicating charset mismatch

## Verdict
- [ ] Verdict chosen: usable-as-is / usable-with-caveats / blocked
- [ ] Top 5 issues written into findings section of the template
