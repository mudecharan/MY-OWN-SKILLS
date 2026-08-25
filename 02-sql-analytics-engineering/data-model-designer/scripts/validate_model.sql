-- data-model-designer · post-load validation queries (run after every load)
-- 1) Grain enforcement: duplicates at declared fact grain must be zero
select order_id, order_line_no, count(*) c
from fact_orders group by 1,2 having count(*) > 1;

-- 2) Orphan foreign keys (broken dimension references)
select f.order_id
from fact_orders f
left join dim_customer d on f.customer_sk = d.customer_sk
where d.customer_sk is null;

-- 3) SCD sanity: exactly one current row per natural key
select customer_id, count(*) currents
from dim_customer where is_current group by 1 having count(*) <> 1;

-- 4) Overlapping validity windows (SCD corruption)
select a.customer_id
from dim_customer a join dim_customer b
  on a.customer_id = b.customer_id and a.customer_sk < b.customer_sk
 and a.valid_from < b.valid_to and b.valid_from < a.valid_to;

-- 5) Fact dates outside dimension coverage
select count(*) from fact_orders f
left join dim_date d on f.date_key = d.date_key where d.date_key is null;
