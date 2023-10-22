import sys
from collections import deque
def bfs(start_x, start_y):
    global graph
    global N, M

    mv_point_x = [0, 0, 1, -1]
    mv_point_y = [1, -1, 0, 0] 

    queue = deque([(start_x, start_y)])
    graph[start_x][start_y] = 1 

    while queue:
        
        x, y = queue.popleft()
        for i in range(4):
            tmp_x, tmp_y = x + mv_point_x[i], y + mv_point_y[i]
            
            # [예외처리]
            if tmp_x < 0  or tmp_x > N-1 or tmp_y < 0 or tmp_y > M-1:
                continue

            if not graph[tmp_x][tmp_y]:
                queue.append((tmp_x, tmp_y))
                graph[tmp_x][tmp_y] = 1
 


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    ice_cream_cnt = 0

    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))

    for i in range(N):
        for j in range(M):
            if not graph[i][j]: # 0이면
                bfs(i, j) # bfs 실행
                ice_cream_cnt += 1
    
    print(ice_cream_cnt)
                
    


