-- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회
-- 보호 시작일 순으로 조회
SELECT ins.NAME, ins.DATETIME FROM ANIMAL_INS as ins
left join ANIMAL_OUTS as outs on ins.ANIMAL_ID = outs.ANIMAL_ID
where outs.ANIMAL_ID is null
order by ins.DATETIME asc
limit 3