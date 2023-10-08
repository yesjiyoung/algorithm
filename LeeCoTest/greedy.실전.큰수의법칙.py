import sys

N, M, K = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

# top 3 뽑기
array.sort(reverse=True)
answer = 0

top1, top2 = array[0], array[1]

if top1 != top2: # 다른 경우 ex. top1 = 6, top2 = 5
    share, remainder = M // K, M % K    
    answer += top1 * K * share # 
    answer += top2 * remainder
else: # 같은 경우 ex. top1 = top2 = 2
    answer += top1 * M 
print(answer)