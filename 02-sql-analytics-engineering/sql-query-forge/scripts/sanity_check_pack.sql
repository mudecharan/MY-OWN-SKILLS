-- sql-query-forge · reconciliation & sanity check pack (run against any new metric query)
-- Replace <final_query>, <key>, <metric> with your staged CTE output.

-- 1) Row-count fingerprint per stage (catches fan-out instantly)
with stage_counts as (
    select 'source' as stage, count(*) n from (<source_cte>) s
    union all select 'clean', count(*) from (<clean_cte>) c
    union all select 'final', count(*) from (<final_query>) f
)
select * from stage_counts;
-- source ≈ clean >> final is NORMAL only when final aggregates.

-- 2) Duplicate grain keys
select <key>, count(*) from (<final_query>) group by 1 having count(*) > 1;

-- 3) Reconciliation vs trusted number (finance's spreadsheet / BI tool)
select abs(
    (select sum(<metric>) from (<final_query>)) -
    <trusted_number>
) / <trusted_number> as pct_gap;
-- tolerance: <0.5% → pass; else hunt mapping/timing differences BEFORE explaining.

-- 4) NULL leakage into dimensions
select count_if(<dimension> is null) as null_dims from (<final_query>);

-- 5) Time-boundary double-count probe: shift window by 1 day; totals should move,
--    not duplicate. Run both, diff by key:
--    select a.<key>, a.<metric> - b.<metric> ... compare day-window vs day+1-window overlap rows.
