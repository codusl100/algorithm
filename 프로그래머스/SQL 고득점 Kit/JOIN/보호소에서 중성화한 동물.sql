-- 보호소에 들어올 당시 중성화되지 않았지만 보호소를 나갈 당시 중성화한 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회
-- 이미 중성화: Spayed
-- 보호소 들어온 후 중성화: Neutered
SELECT ins.ANIMAL_ID, ins.ANIMAL_TYPE, ins.NAME FROM ANIMAL_INS as ins
inner join ANIMAL_OUTS as outs on ins.ANIMAL_ID = outs.ANIMAL_ID
where SUBSTR(ins.SEX_UPON_INTAKE, 1, 6) = 'Intact' and (SUBSTR(outs.SEX_UPON_OUTCOME, 1, 8) = 'Neutered' or SUBSTR(outs.SEX_UPON_OUTCOME, 1, 6) = 'Spayed')
order by ins.ANIMAL_ID