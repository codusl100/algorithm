-- USER_INFO 테이블과 ONLINE_SALE 테이블에서 년, 월, 성별 별로 상품을 구매한 회원수를 집계하는 SQL문을 작성해주세요. 
-- 결과는 년, 월, 성별을 기준으로 오름차순 정렬해주세요. 이때, 성별 정보가 없는 경우 결과에서 제외해주세요.
SELECT YEAR(sale.SALES_DATE) as year, MONTH(sale.SALES_DATE) as month, info.GENDER, COUNT(distinct sale.USER_ID) as USERS FROM ONLINE_SALE as sale
join USER_INFO as info on sale.USER_ID = info.USER_ID
WHERE not info.GENDER is null 
GROUP BY year, month, info.GENDER
ORDER BY year, month, info.GENDER