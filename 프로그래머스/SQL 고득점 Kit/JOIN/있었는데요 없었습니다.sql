-- 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름 조회
SELECT ins.ANIMAL_ID, ins.NAME FROM ANIMAL_INS as ins
left join ANIMAL_OUTS as outs on ins.ANIMAL_ID = outs.ANIMAL_ID
where ins.DATETIME > outs.DATETIME
order by ins.DATETIME asc