select f.category, x.price as max_price, f.product_name
from (
    SELECT category, max(price) as price
    from food_product
    group by category
) as x, food_product as f
where x.category = f.category and f.category in ('과자', '국', '김치', '식용유') and f.price = x.price
group by category
order by max_price desc