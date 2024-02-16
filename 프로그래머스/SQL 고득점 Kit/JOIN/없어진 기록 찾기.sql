-- 1. select에서 불러오는 첫 테이블을 ANIMALS_OUT이라고 함
-- 2. right join이 아닌 inner join으로 함 (inner join하면 당연히 틀리는 게 공통 id값만 추리기 때문..)
-- => join에 대한 명확한 이해 필요

SELECT outs.ANIMAL_ID, outs.NAME FROM ANIMAL_INS as ins
right join ANIMAL_OUTS as outs on ins.ANIMAL_ID = outs.ANIMAL_ID
where ins.ANIMAL_ID is null

-- 얘도 정답 코드
-- SELECT outs.ANIMAL_ID, outs.NAME FROM ANIMAL_OUTS as outs
-- left join ANIMAL_ins as ins on ins.ANIMAL_ID = outs.ANIMAL_ID
-- where ins.ANIMAL_ID is null

-- 1. LEFT JOIN: A, B 테이블 중에 A값의 전체와, A의 KEY 값과 B KEY 값이 같은 결과를 리턴
-- 2. RIGHT JOIN: A, B 테이블 중에 B값의 전체와, B의 KEY 값과 A KEY 값이 같은 결과를 리턴
-- -> 헷갈리면 방향이 향하는 쪽이 항상 기준이라 생각하자