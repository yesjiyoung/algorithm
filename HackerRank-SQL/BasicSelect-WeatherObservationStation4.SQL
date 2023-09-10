-- Q. 
--- Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.

-- A.
select COUNT(CITY) - COUNT(DISTINCT CITY)
from STATION;

-- Note.
--- 집계함수 COUNT : 행 개수 구하기 
--- SELECT COUNT(열1), COUNT(열2) FROM 테이블 명→ 별도로 개수를 셈, NULL은 세지 않음