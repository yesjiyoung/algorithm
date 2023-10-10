import sys

if __name__=='__main__':
    night_pos=sys.stdin.readline()
    
    alpabet_dir_dic ={ alpabet : i+1 for i, alpabet in enumerate('abcdefgh')}
    x, y = alpabet_dir_dic[night_pos[0]], int(night_pos[1])
    
    move_point_x = [-2, -2, 2, 2, 1, -1, 1, -1] # 상상하하좌좌우우
    move_point_y = [1, -1, 1, -1, -2, -2, 2, 2]

    count = 0

    for i in range(len(move_point_x)):
        tmp_x, tmp_y = x + move_point_x[i], y + move_point_y[i]
        
        if tmp_x < 1 or tmp_x > 8 or tmp_y < 1 or tmp_y >8:
            continue 
        
        count+=1
        
    print(count)