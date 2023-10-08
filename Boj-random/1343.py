import sys 

def is_true_case(n):
    p, q = 0, 0
    
    while(True):
        if p >= 50: break
        q = (n - 4*p) / 2
        isInt=int(q) == q 
        if isInt: 
            return True
        p += 1
    return False

def get_polyomino(n):
    # p4 + 2q = n
    a_quotient, a_remainder = n // 4, n % 4
    if a_remainder == 0:
        return 'AAAA' * a_quotient + '.'
    elif a_quotient == 0 and  a_remainder != 0:
        return 'BB' + '.'
    else:
        return 'AAAA' * a_quotient + 'BB'  + '.'


if __name__ == '__main__':
    board=sys.stdin.readline().rstrip()
    answer = ''
    flag = True
    for part in board.split('.'):
        
        part_len = len(part)

        if part_len == 0:
            answer += '.'
            continue
         
        if not is_true_case(part_len):
            print(-1)
            flag = False
            break

        answer += get_polyomino(part_len)
    
    if flag : print(answer[:-1])