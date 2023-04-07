select f.product_id, f.product_name, x.amount * f.price as total_sales
from (
    SELECT product_id, sum(amount) as amount
    from food_order 
    where produce_date like '2022-05%'
    group by product_id
) as x, food_product as f
where f.product_id = x.product_id
order by total_sales desc, product_id