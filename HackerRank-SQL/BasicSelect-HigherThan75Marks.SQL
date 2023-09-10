-- Q.
--- Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name.
--- If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

-- A.
select name 
from students
where marks > 75 
order by right(name, 3), id

-- Note.
--- 부분문자열 가져오기
--- LEFT : 문자열의 왼쪽을 기준으로 n개의 문자를 가져온은 함수  
---- ex. LEFT(컬럼명, n)
--- MID : 문자열에서 지정한 시작 위치를 기준으로 n개의 문자를 가져오는 함수 (=substr, substring)
---- ex. MID(컬럼명, 시작위치, n), SUBSTR(컬럼명, 시작위치, n), SUBSTRING(컬럼명, 시작위치, n)
--- RIGHT : 문자열의 오른쪽을 기준으로 n개의 문자를 가져오는 함수 
---- ex. RIGHT(컬럼명, n)