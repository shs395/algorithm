select concat('/home/grep/src/', a.board_id, '/', a.file_id, a.file_name, a.file_ext) as file_path
from (
    SELECT board_id 
    from used_goods_board 
    order by views desc
    limit 1
) as x, USED_GOODS_FILE as a
where x.board_id = a.board_id
order by a.file_id desc
