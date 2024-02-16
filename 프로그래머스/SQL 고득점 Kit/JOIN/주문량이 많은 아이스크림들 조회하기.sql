-- 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회
SELECT f.FLAVOR 
FROM FIRST_HALF as f join 
(SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER FROM JULY GROUP BY FLAVOR) as j on f.FLAVOR = j.FLAVOR
order by (j.TOTAL_ORDER + f.TOTAL_ORDER) desc
limit 3