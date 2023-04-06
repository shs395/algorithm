SELECT 
    user_id, 
    nickname, 
    concat(city, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) as 전체주소, 
    concat(substr(TLNO,1,3), '-', substr(TLNO,4,4), '-', substr(TLNO,8,4)) as 전화번호
from used_goods_board as b
    inner join used_goods_user as u
    on b.writer_id = u.user_id
group by b.writer_id
having count(*) >= 3
order by user_id desc