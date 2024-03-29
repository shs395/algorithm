SELECT ingredient_type, sum(total_order) as TOTAL_ORDER
from first_half
    inner join icecream_info
    on first_half.flavor = icecream_info.flavor
group by ingredient_type
order by TOTAL_ORDER