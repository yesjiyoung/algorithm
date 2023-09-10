--- Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.
--- 짝수, 홀수 판단 -> MOD
select distinct CITY
from STATION
where MOD(ID, 2) = 0;