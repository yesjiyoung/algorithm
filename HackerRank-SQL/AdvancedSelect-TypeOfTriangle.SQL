select 
case 
when A = B and B = C then 'Equilateral'
when (A >= B+C) or (B >= A+C) or (C >=A+B) then 'Not A Triangle'
when A=B or A=C or B=C then 'Isosceles'
else 'Scalene' 
end 
from TRIANGLES;
-- CASE WHEN ~~ THEN ~~ ELSE END  
