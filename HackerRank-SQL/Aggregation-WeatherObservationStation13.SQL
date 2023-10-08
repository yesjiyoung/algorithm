select truncate(sum(lat_n),4)
from station
where lat_n > 38.7880 and lat_n < 137.2345

-- truncate(column, 4) # 4개 밑으로는 버리기 