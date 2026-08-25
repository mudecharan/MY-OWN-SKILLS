-- ============================================================
-- dbt-transformation-guide · reference model with tests (marts layer)
-- File: models/marts/fct_orders.sql  |  config materialized=incremental
-- ============================================================

{{ config(
    materialized = 'incremental',
    unique_key   = 'order_line_sk',
    on_schema_change = 'fail'
) }}

with orders as (
    select * from {{ ref('stg_orders') }}
    {% if is_incremental() %}
    where updated_at > (select coalesce(max(updated_at), '1970-01-01') from {{ this }})
    {% endif %}
),

order_items as (
    select * from {{ ref('stg_order_items') }}
),

final as (
    select
        o.order_id,
        oi.order_line_no,
        o.customer_id,
        date_trunc('day', o.ordered_at) as order_date,
        oi.quantity,
        oi.unit_price,
        oi.quantity * oi.unit_price     as line_revenue,
        o.updated_at
    from orders o
    join order_items oi using (order_id)
)

select * from final

-- Business logic lives in intermediate CTEs; staging stays 1:1 light transforms.
