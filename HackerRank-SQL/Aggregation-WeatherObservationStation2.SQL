select round(sum(LAT_N),2), round(sum(LONG_W),2)
from station

-- round('컬럼', 남는마지막자릿수)