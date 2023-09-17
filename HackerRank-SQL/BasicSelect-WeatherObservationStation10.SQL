-- Q. Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.

-- A.
select distinct city 
from station
where city regexp '[^aeiou]$'

-- Note.
--- BasicSelect-WeatherObservationStation6 참고