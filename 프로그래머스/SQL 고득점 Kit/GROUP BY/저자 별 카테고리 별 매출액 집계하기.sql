-- 2022년 1월의 도서 판매 데이터를 기준으로 저자 별, 카테고리 별 매출액(TOTAL_SALES = 판매량 * 판매가) 을 구하여, 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES) 리스트를 출력하는 SQL문을 작성해주세요.
-- 결과는 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬해주세요
SELECT b.author_id, b.author_name, a.category, (sum(c.sales*a.price)) as total_sales
from book a, author b, book_sales c
where a.book_id=c.book_id and a.author_id=b.author_id and date_format(sales_date,'%Y-%m-%d') like '2022-01%'
group by a.category, b.author_name
order by b.author_id, a.category desc