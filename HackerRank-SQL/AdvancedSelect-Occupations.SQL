select MAX(IF(occupation = "DOCTOR", NAME, NULL)) AS DOCTOR,
       MAX(IF(occupation = "PROFESSOR", NAME, NULL)) AS PROFESSOR,
       MAX(IF(occupation = "SINGER", NAME, NULL)) AS SINGER,
       MAX(IF(occupation = "ACTOR", NAME, NULL)) AS ACTOR
from 
(select name,
        occupation, 
        row_number() Over (Partition By occupation ORDER BY name) as row_num 
  from occupations) as t 
group by row_num;

-- 자세히 : https://didu-story.tistory.com/95
-- row_number() over (partition by occpation order by name)