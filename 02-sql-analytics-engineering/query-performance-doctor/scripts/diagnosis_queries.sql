-- ============================================================
-- query-performance-doctor · diagnosis starter queries
-- Uncomment the block matching your platform.
-- ============================================================

-- ---------- SNOWFLAKE: most expensive queries last 7d ----------
-- select query_text, total_elapsed_time/1000 as sec,
--        bytes_scanned/1e9 as gb_scanned, credits_used_cloud_services,
--        start_time
-- from snowflake.account_usage.query_history
-- where start_time > dateadd(day,-7,current_timestamp())
-- order by bytes_scanned*count(*) desc limit 20;

-- ---------- SNOWFLAKE: get the execution plan ----------
-- explain using tabular select ... ;

-- ---------- BIGQUERY: top cost queries via INFORMATION_SCHEMA ----------
-- select query, total_bytes_processed/1e9 as gb, timestamp
-- from `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
-- where creation_time > timestamp_sub(current_timestamp(), interval 7 day)
-- order by total_bytes_processed desc limit 20;

-- ---------- POSTGRES: find slow + missing indexes ----------
-- explain (analyze, buffers)
-- select ... ;
-- -- unused/duplicate index candidates:
-- select relname, indexrelname, idx_scan
-- from pg_stat_user_indexes order by idx_scan asc limit 20;

-- ---------- Generic anti-pattern probes to run on the slow query ----
-- 1) Function on the filtered column kills sargability:
--    BAD:  where date(created_at) = current_date
--    GOOD: where created_at >= current_date and created_at < current_date + interval '1 day'
-- 2) Join explosion check — compare counts at each stage:
--    select count(*) from a;                      -- expect N
--    select count(*) from a join b using (k);     -- if >> N, fan-out bug
-- 3) Pre-aggregate before joining big facts:
--    with agg as (select k, sum(v) v from fact group by k)
--    select ... from dim d join agg a using (k);
