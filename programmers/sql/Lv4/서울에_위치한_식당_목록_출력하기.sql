SELECT ri.rest_id, ri.rest_name, ri.food_type, ri.favorites, ri.address, round(avg(rr.review_score), 2) as score
from rest_info as ri, rest_review as rr
where ri.address like '서울%' and ri.rest_id = rr.rest_id
group by ri.rest_id
order by score desc, favorites desc
