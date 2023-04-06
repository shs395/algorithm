SELECT ai.name, ai.datetime
from animal_ins as ai
    left outer join animal_outs as ao
    on ai.animal_id = ao.animal_id
    where ao.datetime is null
order by datetime
limit 3