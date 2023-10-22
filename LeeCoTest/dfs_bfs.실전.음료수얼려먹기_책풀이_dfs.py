import sys
from collections import deque

def dfs(x, y):
    global graph
    global N, M

    if x < 0 or x > N-1 or y < 0 or y > M-1:
        return False
    
    if not graph[x][y]:
        graph[x][y] = 1 # 방문 처리 한다.
        # 상, 하, 좌, 우 방문 처리 시작 
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    
    return False

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    ice_cream_cnt = 0

    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))

    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                ice_cream_cnt +=1
    
    print(ice_cream_cnt)