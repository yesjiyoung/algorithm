--- 오라클에서만 Median() 사용 가능 
--- mysql은 아주 복잡함 
select round(median(lat_n),4)
from station