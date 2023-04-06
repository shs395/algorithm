select id, name, x.host_id
from (
    SELECT host_id
    from places
    group by host_id
    having count(*) >= 2
) as x, places as p
where p.host_id = x.host_id
order by id
