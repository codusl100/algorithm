-- 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회
-- 회원 이름, 리뷰 텍스트, 리뷰 작성일 출력하고 결과는 리뷰 작성일 기준으로 오름차순, 같다면 리뷰 텍스트 기준 오름차순
SELECT m.MEMBER_NAME, r.REVIEW_TEXT, DATE_FORMAT(r.REVIEW_DATE, "%Y-%m-%d") FROM MEMBER_PROFILE as m
join REST_REVIEW as r on m.MEMBER_ID = r.MEMBER_ID
WHERE m.MEMBER_ID = 
(SELECT MEMBER_ID FROM REST_REVIEW GROUP BY MEMBER_ID order by COUNT(MEMBER_ID) desc limit 1)
order by r.REVIEW_DATE asc, r.REVIEW_TEXT asc
