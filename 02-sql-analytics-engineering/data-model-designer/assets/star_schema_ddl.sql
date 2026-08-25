-- ============================================================
-- data-model-designer · star schema DDL template (Postgres flavor)
-- One fact table per business process; conformed dimensions shared.
-- ============================================================

-- Dimension with Type-2 history
create table dim_customer (
    customer_sk      bigserial primary key,          -- surrogate key
    customer_id      text not null,                  -- natural/business key
    full_name        text,
    segment          text,
    region           text,
    -- SCD Type-2 columns:
    valid_from       timestamptz not null,
    valid_to         timestamptz not null default 'infinity',
    is_current       boolean not null default true,
    _loaded_at       timestamptz not null default now()
);
create index on dim_customer (customer_id, is_current);

-- Date dimension (generate once)
create table dim_date (
    date_key    int primary key,          -- yyyymmdd
    date_actual date not null unique,
    year int, quarter int, month int, month_name text,
    day_of_week int, day_name text, is_weekend boolean,
    fiscal_year int, fiscal_quarter text
);

-- Fact table at declared atomic grain: one row per ORDER LINE
create table fact_orders (
    order_line_sk  bigserial primary key,
    order_id       text not null,             -- degenerate dimension
    order_line_no  int  not null,
    customer_sk    bigint not null references dim_customer(customer_sk),
    date_key       int    not null references dim_date(date_key),
    quantity       int    not null check (quantity >= 0),
    unit_price     numeric(12,2) not null,
    line_revenue   numeric(14,2) not null,
    _loaded_at     timestamptz not null default now(),
    unique (order_id, order_line_no)          -- idempotency guard
);

-- Typical query becomes trivial (vs 8-way join mess):
-- select d.month_name, sum(f.line_revenue)
-- from fact_orders f join dim_date d using (date_key)
-- where f.date_key between 20240101 and 20241231 group by 1;

-- SCD Type-2 update pattern (run in load job):
-- update dim_customer set is_current=false, valid_to=now()
--  where customer_id=:id and is_current;
-- insert into dim_customer (customer_id, full_name, segment, region, valid_from)
-- values (:id,:name,:segment,:region, now());
