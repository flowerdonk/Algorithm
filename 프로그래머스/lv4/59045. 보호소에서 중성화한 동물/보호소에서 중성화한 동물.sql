-- 보호소에서 중성화 수술을 거친 동물
-- 보호소에 들어올 당시에는 중성화되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물
-- 아이디와 생물 종, 이름을 조회
-- 아이디 순으로 조회

SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.SEX_UPON_INTAKE LIKE 'Intact%' AND (O.SEX_UPON_OUTCOME LIKE 'Spayed%' OR O.SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY I.ANIMAL_ID;