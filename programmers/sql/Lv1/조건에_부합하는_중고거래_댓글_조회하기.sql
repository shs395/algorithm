SELECT ugb.title, ugb.board_id, ugr.reply_id, ugr.writer_id, ugr.contents, date_format(ugr.created_date, '%Y-%m-%d')
from 
    used_goods_board as ugb,
    used_goods_reply as ugr
where 
    ugb.created_date like '2022-10%' and
    ugb.board_id = ugr.board_id
order by ugr.created_date, ugb.title