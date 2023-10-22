# 바다는 갈 수 없음
# 캐릭터가 방문한 칸의 수를 출력 
import sys

def go_left(current_x, current_y, current_d):
    """왼쪽으로 방향을 변경하고, 왼쪽으로 위치를 바꾸는 함수"""
    
    if current_d == 0: current_y -= 1 # 북방향에서 왼쪽
    elif current_d == 1: current_x -= 1 #동방향에서 왼쪽 
    elif current_d == 2: current_y += 1
    else: 
        current_x += 1

    current_d = change_directions[current_d]
    
    return current_x, current_y, current_d

def change_direction(current_d):
    """방향을 바꾸는 함수"""
    global change_directions

    return change_directions[current_d]


def go_back(current_x, current_y, current_d):
    """바라보고 있는 방향은 유지한채, 뒤로 위치를 바꾸는 함수"""
    
    if current_d == 0: current_x += 1 # 북방향에서 뒤로 
    elif current_d == 1: current_y -= 1 #동방향에서 뒤로 
    elif current_d == 2: current_x -= 1 #남방향에서 뒤로
    else: current_y += 1 # 서방향에서 뒤로 
    
    return current_x, current_y, current_d


def is_all_sea_or_visited(current_x, current_y, current_d):
    global map
    
    if map[current_x-1][current_y] and map[current_x+1][current_y] \
        and map[current_x][current_y-1] and map[current_x][current_y+1]:
        return True
    return False


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    x, y, d = map(int, sys.stdin.readline().split()) # 1, 1, 0
    
    directions = {0 : (-1, 0), 1 : (0, 1), 2 : (-1, 0), 3 : (0, -1)} # 북, 동, 남, 서 
    change_directions = { 0:3, 1:0, 2:1, 3:2}

    map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # Map 정의 
    #visited = [[False] * M for _ in range(N)] # 방문 체크 용도
    map[x][y] = 1

    count = 1
    flag = 0
    while(True):
        print(f"x, y, d : {x}, {y}, {d}")

        # 예외) 사방이 방문했던 곳이거나 방문하려는 곳이 바다인 경우
        if is_all_sea_or_visited(x,y,d): # 방문했거나 바다라면 
            x, y, d = go_back(x, y, d) # 뒤로 이동 
            if x < 0 or x > N-1 or y < 0 or y > M - 1 or map[x][y]: # 뒤로이동했는데 바다면 종료
                break
            continue

        tmp_x, tmp_y, tmp_d = go_left(x, y, d)
        # 예외) 만일 가려는 곳이 바다이거나 방문했던 곳이거나 바다인 경우, 방향만 바꿔주기
        if tmp_x < 0 or tmp_x > N -1 or tmp_y < 0 or tmp_y > M -1  or map[tmp_x][tmp_y]:
            d = tmp_d
            continue
        
        # 위치 및 방향 업데이트 
        x, y, d = tmp_x, tmp_y, tmp_d
        map[x][y] = True
        count +=1


    print(count)




