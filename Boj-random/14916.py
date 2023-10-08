import sys

remains = int(sys.stdin.readline())
count = 0

while True:
    if remains % 5 == 0 : # 5의 배수이면 
        count += remains // 5
        break

    else: # 5의 배수가 아니라면, 2씩 빼기 
        remains -= 2 
        count += 1
    
    if remains < 0:
        break

if remains <0 : print(-1)
else: print(count)