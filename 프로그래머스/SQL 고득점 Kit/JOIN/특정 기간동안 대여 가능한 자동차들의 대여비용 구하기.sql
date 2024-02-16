-- 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서
-- 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력하는 SQL문
-- 대여 금액을 기준으로 내림차순 정렬하고, 대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬, 자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순
SELECT car.CAR_ID, car.CAR_TYPE, FLOOR(30 * car.DAILY_FEE * (1 - plan.DISCOUNT_RATE/100)) as FEE FROM CAR_RENTAL_COMPANY_CAR as car
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as plan on car.CAR_TYPE = plan.CAR_TYPE and plan.DURATION_TYPE = '30일 이상' and car.CAR_TYPE in ('세단', 'SUV')
left join CAR_RENTAL_COMPANY_RENTAL_HISTORY as history on car.CAR_ID = history.CAR_ID and history.END_DATE >= '2022-11-01' and history.START_DATE <= '2022-11-30'
where round(30 * car.DAILY_FEE * (1 - plan.DISCOUNT_RATE/100)) BETWEEN 500000 AND 1999999 and history.CAR_ID is null
order by FEE desc, car.CAR_TYPE asc, car.CAR_ID desc