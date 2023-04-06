select 
    case
        when start_date like '2022-08%'
        then 8
        when start_date like '2022-09%'
        then 9
        when start_date like '2022-10%'
        then 10
    end as MONTH,
    h.car_id,
    count(*) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as h, (
    SELECT car_id
    from car_rental_company_rental_history
    where start_date >= '2022-08-01' and start_date <= '2022-10-31'
    group by car_id
    having count(*) >= 5
) as x
where x.car_id = h.car_id and h.start_date >= '2022-08-01' and h.start_date <= '2022-10-31'
group by h.car_id, month
having count(*) > 0
order by month, car_id desc