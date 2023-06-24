-- 몇 시에 입양이 가장 활발한지
-- 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회
-- 결과는 시간대 순으로 정렬

SET @time := -1;

SELECT (@time := @time + 1) HOUR, (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @time) COUNT FROM ANIMAL_OUTS
WHERE @time < 23;