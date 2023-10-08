select months * salary as earnings, count(*) as cnt
from employee
group by earnings
order by earnings desc 
limit 1
