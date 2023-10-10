import sys 

def is_out_point(point):
    global N
    x, y = point[0], point[1]
    if x < 1 or x > N or y < 1 or y > N: return True
    return False

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    roots = sys.stdin.readline().split()
    
    current_point, final_point = (1, 1), (N, N) # (5, 5)
    direction = {"L" : (0,-1), "R" : (0, 1), "U" : (-1, 0), "D" : (1,0)}

    for root in roots:
        new_point = tuple(sum(elem) for elem in zip(current_point, direction[root]))
        if not is_out_point(new_point):
            current_point = new_point

    print(current_point[0], current_point[1], sep=' ')