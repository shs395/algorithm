SELECT ai.animal_id, ai.animal_type, ai.name
from animal_ins as ai
    left join animal_outs as ao
    on ai.animal_id = ao.animal_id
where ai.sex_upon_intake like '%Intact%' and (ao.SEX_UPON_OUTCOME like '%Spayed%' or ao.SEX_UPON_OUTCOME like '%Neutered%')
order by ai.animal_id