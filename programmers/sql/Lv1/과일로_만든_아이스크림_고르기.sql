select fh.flavor 
from first_half as fh, icecream_info as ii 
where fh.flavor = ii.flavor and fh.total_order > 3000 and ii.ingredient_type = 'fruit_based'
order by fh.total_order desc