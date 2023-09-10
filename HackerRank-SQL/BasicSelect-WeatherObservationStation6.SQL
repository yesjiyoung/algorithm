-- Q. Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates

-- A1.
select distinct city
from STATION
where city like "a%" 
or city like "e%"
or city like "i%"
or city like "o%"
or city like "u%"

-- A2.
select distinct city
from STATION
where city REGEXP '^[aeiou]'

-- NOTE.
--- 패턴 매칭에 의한 검색 : LIKE 
---- % 사용 
----- 'SQL%' : SQL로 시작하는 string 
----- '%SQL%' : 중간에 SQL이 들어가는 string 
----- '%SQL' : SQL로 끝나는 string 
---- _ 사용
----- 'S__' : S로 시작하는 세글자 문자

--- 정규 표현식 : REGEXP
---- : LIKE 보다 복잡한 문자열 조건으로 검색 가능 (자세히 : https://junyoung-developer.tistory.com/34)
