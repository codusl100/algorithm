-- PRODUCT 테이블과 OFFLINE_SALE 테이블에서 상품코드 별 매출액(판매가 * 판매량) 합계를 출력
-- 매출액을 기준으로 내림차순 정렬해주시고 매출액이 같다면 상품코드를 기준으로 오름차순 정렬
SELECT p.PRODUCT_CODE, SUM(p.PRICE * o.SALES_AMOUNT) as SALES FROM PRODUCT as p
join OFFLINE_SALE as o on p.PRODUCT_ID = o.PRODUCT_ID
group by p.PRODUCT_CODE
order by SALES desc, p.PRODUCT_CODE asc