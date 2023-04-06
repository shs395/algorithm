SELECT 
    x.car_id,
    case 
        when sum(AVAILABILITY) > 0
        then '대여중'
        else '대여 가능'
    end as AVAILABILITY
from (
    select 
        car_id,
        case 
            when "2022-10-16" between START_DATE and END_DATE
            then 1
            else 0
        end as AVAILABILITY
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
) as x
group by car_id
order by car_id desc