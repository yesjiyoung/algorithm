import sys
from collections import deque



if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())

    # 미로 정의
    miro = []
    for i in range(N):
        miro.append(list(map(int, input())))
    
    direction_x = [-1, 1, 0, 0]
    direction_y = [0, 0, -1, 1]


    queue = deque([(0,0)]) # 큐에 넣고 

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            
            tmp_x, tmp_y = x + direction_x[i], y + direction_y[i]
            
            # 예외처리 
            if tmp_x < 0 or tmp_x > N -1 or tmp_y < 0 or tmp_y > M-1:
                continue
            if not miro[tmp_x][tmp_y]:
                continue
            
            if miro[tmp_x][tmp_y] == 1: # 1이면 
                miro[tmp_x][tmp_y] = miro[x][y] + 1
                queue.append((tmp_x, tmp_y)) # 큐에 넣고
                
    print(miro[N-1][M-1])

    

