"""cloud-warehouse-cost-optimizer · consumption audit queries (Snowflake/BigQuery/Postgres).
Run the block for your platform; paste results into assets/cost_audit_template.md.
"""
-- ============ SNOWFLAKE ============
-- Top cost culprits: expensive × frequent
-- select left(query_text, 80) as query_snippet,
--        count(*) as executions,
--        sum(total_elapsed_time)/1000/1000 as total_hours,
--        sum(bytes_scanned)/1e12 as tb_scanned,
--        avg(total_elapsed_time)/1000 as avg_sec
-- from snowflake.account_usage.query_history
-- where start_time > dateadd(day, -30, current_timestamp())
-- group by 1 order by tb_scanned desc limit 20;

-- Warehouse sizing check (utilization while running)
-- select warehouse_name, avg(avg_running) as avg_load,
--        max(size) / min(size) as size_variability
-- from snowflake.account_usage.warehouse_load_history
-- where start_time > dateadd(day, -14, current_timestamp())
-- group by 1;

-- Storage: biggest tables & Time Travel overhead
-- select table_name, active_bytes/1e9 gb,
--        time_travel_bytes/1e9 tt_gb, retention_target_days
-- from snowflake.account_usage.table_storage_metrics
-- order by active_bytes desc limit 20;

-- ============ BIGQUERY ============
-- select user_email, count(*) jobs,
--        sum(total_bytes_processed)/pow(10,12) tb,
--        sum(total_slot_ms)/1000 slot_s
-- from `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
-- where creation_time > timestamp_sub(current_timestamp(), interval 30 day)
--   and job_type = 'QUERY'
-- group by 1 order by tb desc limit 20;

-- ============ GENERIC ANTI-PATTERN PROBES ============
-- SELECT * frequency:
--   ... where query_text ilike 'select *%' group by 1;
-- Identical repeated queries (cache/materialization candidates):
--   select query_hash, count(*) c from history group by 1 having c > 50;
-- Dashboard refresh storms: same query per minute from BI service account.
