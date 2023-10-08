import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_num = 0
for line in board:
    if max_num < min(line):
        max_num = min(line)
print(max_num)
    