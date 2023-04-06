SELECT a.food_type, a.rest_id, a.rest_name, a.favorites
from rest_info as a, (
    select food_type, max(favorites) as favorites
    from rest_info
    group by food_type
    order by favorites desc
) as b
where a.food_type = b.food_type and a.favorites = b.favorites
order by food_type desc