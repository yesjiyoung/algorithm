import sys
from itertools import combinations
shorter_boys_heights = [int(sys.stdin.readline()) for _ in range(9)]
for comb in combinations(shorter_boys_heights, 7):
    if sum(comb) == 100:
        comb_list=sorted(list(comb))
        print(*comb_list, sep='\n')
        break