-- Q. Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

-- A1.
select distinct CITY
from STATION
where CITY LIKE "%a" 
or CITY LIKE "%e"
or CITY LIKE "%i"
or CITY LIKE "%o"
or CITY LIKE "%u"

-- A2.
select distinct CITY
from STATION
where CITY REGEXP '[aeiou]$'

-- Note.
--- BasicSelect-WeatherObservationStation6 참고