import sys

def isThree(x):
    if '3' in str(x): return True
    return False

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    cnt = 0

    for h in range(N+1):
        for m in range(60):
            for s in range(60):
                #print(f"{h}:{m}:{s}")
                if isThree(h) or isThree(m) or isThree(s): 
                    cnt +=1

    print(cnt)

                
