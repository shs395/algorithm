SELECT h.car_id
from car_rental_company_rental_history as h
    left outer join car_rental_company_car as c
    on h.car_id = c.car_id
where car_type = '세단' and start_date like '2022-10%'
group by h.car_id
order by h.car_id desc