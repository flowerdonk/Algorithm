-- 2021년에 가입한 전체 회원들 중 상품을 구매한 회원수와 상품을 구매한 회원 비율
-- 비율 = 2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수
-- 소수점 두번째자리에서 반올림
-- 년, 월 별로 출력
-- 년을 기준으로 오름차순, 년이 같다면 월을 기준으로 오름차순 정렬

SELECT YEAR, MONTH, COUNT(*) AS PURCHASED_USERS, 
ROUND((COUNT(*) / (SELECT COUNT(*) FROM USER_INFO WHERE YEAR(JOINED) = 2021)), 1) AS PURCHASED_RATIO
FROM (
    SELECT DISTINCT YEAR(S.SALES_DATE) AS YEAR, MONTH(S.SALES_DATE) AS MONTH, U.USER_ID
    FROM ONLINE_SALE AS S
    JOIN USER_INFO AS U ON S.USER_ID = U.USER_ID
    WHERE YEAR(U.JOINED) = 2021
) A
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH;