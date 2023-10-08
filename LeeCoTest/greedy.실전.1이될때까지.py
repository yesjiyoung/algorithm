import sys
N, K = map(int, sys.stdin.readline().split())

cnt=0
while True:
    if N <= 0: 
        break
    
    share, remainders = N // K, N % K 
    if remainders == 0:
        cnt +=1
        N = share
    else:
        N -= 1

print(cnt)
