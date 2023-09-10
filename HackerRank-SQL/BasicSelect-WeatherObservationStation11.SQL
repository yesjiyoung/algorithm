-- Q. Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

-- A. 
SELECT DISTINCT CITY 
FROM STATION
WHERE CITY REGEXP '^[^aeoui]' or CITY REGEXP '[^aeoui]$'

-- Note.
--- BasicSelect-WeatherObservationStation6 참고