SELECT book_id, author_name, date_format(published_date, '%Y-%m-%d') as PUBLISHED_DATE
from book 
    inner join author
    on book.author_id = author.author_id
where book.category = '경제'
order by published_date