-- USED_GOODS_BOARD와 USED_GOODS_USER 테이블에서 완료된 중고 거래의 총금액이 70만 원 이상인 사람의 회원 ID, 닉네임, 총거래금액을 조회하는 SQL문을 작성해주세요. 
-- 결과는 총거래금액을 기준으로 오름차순 정렬해주세요.
SELECT USER_ID, NICKNAME, SUM(PRICE) as TOTAL_SALES FROM USED_GOODS_USER as us
JOIN USED_GOODS_BOARD as board on board.WRITER_ID = us.USER_ID
WHERE board.STATUS = 'DONE'
GROUP BY board.WRITER_ID
HAVING SUM(PRICE) >= 700000
ORDER BY TOTAL_SALES