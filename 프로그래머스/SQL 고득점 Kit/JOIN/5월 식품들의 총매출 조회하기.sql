-- FOOD_PRODUCT와 FOOD_ORDER 테이블에서 생산일자가 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회
-- 총매출을 기준으로 내림차순 정렬, 총매출이 같다면 식품 ID를 기준으로 오름차순 정렬
SELECT p.PRODUCT_ID, p.PRODUCT_NAME, SUM(p.PRICE * o.AMOUNT) as TOTAL_SALES FROM FOOD_PRODUCT as p
join FOOD_ORDER as o on p.PRODUCT_ID = o.PRODUCT_ID
where SUBSTR(o.PRODUCE_DATE, 1,7) = '2022-05'
group by p.PRODUCT_NAME
order by TOTAL_SALES desc, p.PRODUCT_ID asc