-- Q. Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

-- A. 
select distinct city
from station 
where city REGEXP '^[^aeoui]'

-- Note.
--- BasicSelect-WeatherObservationStation6 참고