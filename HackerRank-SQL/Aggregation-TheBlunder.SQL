select ceil(avg(salary) - avg(cast(replace(cast(salary as char(10)), '0', '') as unsigned)))
from employees

-- ceil 가까운 정수로 올림 
-- cast(colum as unsigned ) 문자를 interger로 바꿈 
-- cast(colum as char(10)) 숫자를 문자열로 바꿈 
-- replace(column, 'A', 'B') 'A'문자를 'B'로 바꿈 