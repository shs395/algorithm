SELECT c.cart_id
from (
    SELECT * 
    from cart_products
    where name like 'Milk'    
) as x, cart_products as c
where c.name like 'Yogurt' and x.cart_id = c.cart_id
order by c.cart_id