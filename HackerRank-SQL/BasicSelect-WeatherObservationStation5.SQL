-- Q.
--- Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). 
--- If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

-- A. 
select city, length(city)
from station
order by length(city), city
limit 1;

select city, length(city)
from station
order by length(city) desc, city
limit 1;

-- Note.
--- 정렬 : order by 
----- asc(오름차순), desc(내림차순)
----- 복수의 열로 정렬 가능 : SELECT 열 FROM 테이블명 WHERE 조건식 ORDER BY 열1 (정렬방식), 열2 (정렬방식)
--- 행개수 제한 : limit 
----- SELECT 열 FROM 테이블명 WHERE 조건식 ORDER BY LIMIT 행수 [OFFSET 시작행] : OFFSET 기본 값 : 0 LIMIT 3 (1, 2, 3 행) / LIMIT 3 OFFSET 3 (4, 5, 6 행)
