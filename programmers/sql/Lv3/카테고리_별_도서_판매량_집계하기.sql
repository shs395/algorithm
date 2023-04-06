SELECT category, sum(book_sales.sales) as TOTAL_SALES
from book_sales
    inner join book
    on book.book_id = book_sales.book_id
where book_sales.sales_date like '2022-01%'
group by book.category
order by book.category