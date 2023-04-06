SELECT ai.animal_id, ai.name
from animal_ins as ai
    inner join animal_outs as ao
    on ai.animal_id = ao.animal_id
where ai.datetime > ao.datetime
order by ai.datetime