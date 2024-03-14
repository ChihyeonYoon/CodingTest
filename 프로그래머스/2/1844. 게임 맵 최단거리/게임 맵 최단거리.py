def solution(maps):
    answer = []

    ver_len = len(maps)
    horiz_len = len(maps[0])

    from collections import deque
    visited = {}
    q = deque()
    q.append((0,0,1))

    while q:
        cur = q.popleft()
        x,y,a = cur
        
        if (x,y) in visited:
            continue

        if y<0 or y>ver_len-1 or x<0 or x>horiz_len-1:
            continue
        
        if maps[y][x] == 0:
            continue
        
        if maps[y][x] == 1:
            print(x,y,':',a)
            # answer += 1
            visited[(x,y)]=a
            if y == ver_len-1 and x == horiz_len-1:
                print("End Point")
                continue

            q.append((x+1,y,a+1))#right_pt
            q.append((x-1,y,a+1))#left_pt 
            q.append((x,y+1,a+1))#down_pt 
            q.append((x,y-1,a+1))#up_pt 

    return visited[(horiz_len-1, ver_len-1)] if (horiz_len-1, ver_len-1) in visited else -1
