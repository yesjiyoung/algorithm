import sys
from collections import deque

def dfs(start_node):
    
    dfs_visited[start_node] = True
    print(start_node, end=' ')

    # 현재 노드와 연결된 노드를 재귀적으로 호출
    for node in range(1, len(matrix)):
        if matrix[start_node][node] and not dfs_visited[node]:
            dfs(node)


def bfs(start_node):
    #visited = [ False for _ in range(len(matrix))]
    current_queue = deque([start_node]) # 큐에 넣고 
    bfs_visited[start_node] = True
    debugging_for_visit_node_sequence = [start_node]

    while(current_queue):
        target_node = current_queue.popleft()
        for node, state in enumerate(matrix[target_node]):
            if state and not bfs_visited[node]: 
                current_queue.append(node) # 넣고
                bfs_visited[node] = True
                debugging_for_visit_node_sequence.append(node)
                #matrix[target_node][node], matrix[node][target_node] = 0, 0  # 방문처리하고
    
    print(*debugging_for_visit_node_sequence)

if __name__ == '__main__':
    N, M, V = map(int, sys.stdin.readline().split())
    # N(노드) : N (1<= N <= 1000)
    # M(간선) : M (1<= M <= 10,000) 
    # 노드 개수 < 간선 개수 -> 인접리스트로 구현 

    matrix = [[0] * (N+1) for _ in range(N+1)] # 일단 0으로 초기화 

    for i in range(M):
        start_node, end_node = map(int, sys.stdin.readline().split())
        matrix[start_node][end_node] = matrix[end_node][start_node] = 1
    
    dfs_visited = [False] *(N+1)
    bfs_visited = [False] *(N+1)
    print(dfs(V))
    print(bfs(V))

