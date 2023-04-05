SELECT car_id, round(avg(datediff(end_date, start_date) + 1), 1) as AVERAGE_DURATION
from car_rental_company_rental_history
group by car_id
having average_duration >= 6
order by average_duration desc, car_id desc