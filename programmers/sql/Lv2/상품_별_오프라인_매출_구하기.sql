SELECT product.product_code, price * sum(sales_amount) as sales
from product
    inner join offline_sale
    on product.product_id = offline_sale.product_id
group by product.product_code
order by sales desc, product.product_code