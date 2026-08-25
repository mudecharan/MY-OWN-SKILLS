-- ============================================================
-- sql-query-forge · layered metric query template
-- Dialect: adapt functions per warehouse (Snowflake/BQ/Postgres)
-- Replace <angle_brackets>; delete stages you don't need.
-- Grain of final output: one row per <GRAIN>
-- ============================================================

with source as (
    select
        o.order_id,
        o.customer_id,
        o.order_ts,                      -- always UTC in raw; convert once, here
        convert_timezone('UTC','America/New_York', o.order_ts) as local_ts,
        oi.product_id,
        oi.quantity,
        oi.unit_price,
        oi.line_revenue
    from {{ ref('stg_orders') }} o
    join {{ ref('stg_order_items') }} oi using (order_id)
    where o.order_ts >= '<start_ts>' and o.order_ts < '<end_ts>'   -- half-open range!
      and o.is_test = false                                        -- exclude test traffic
),

clean as (
    -- grain enforcement: exactly one row per order-item
    select * from (
        select *,
            row_number() over (partition by order_id, product_id order by updated_at desc) as rn
        from source
    ) d
    where rn = 1
      and quantity > 0                 -- edge case: returns handled separately
)

, aggregate as (
    select
        date_trunc('<period>', local_ts)          as period,
        customer_segment,
        count(distinct order_id)                  as orders,
        count(distinct customer_id)               as customers,
        sum(line_revenue)                         as revenue,
        sum(line_revenue) / nullif(count(distinct order_id),0) as aov   -- zero-division guard
    from clean
    group by 1, 2
)

select *
from aggregate
order by period desc;
