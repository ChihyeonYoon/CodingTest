def solution(maps):
    answer = 0
    
    from collections import deque
    
    def bfs(maps, start):
        q = deque([(start, 0)])
        visited = {start: 0}
        
        y_len, x_len = len(maps), len(maps[0])
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
                
        while q:
            cur_pt, cur_depth = q.popleft()
            cur_y, cur_x = cur_pt
            for direction in directions:
                next_y = cur_y + direction[0]
                next_x = cur_x + direction[1]
                if 0 <= next_y < y_len and 0 <= next_x < x_len:
                    if (next_y, next_x) not in visited and maps[next_y][next_x] == 1:
                        next_depth = cur_depth +1
                        visited[(next_y, next_x)] = next_depth
                        q.append(((next_y, next_x), next_depth))
                
        return visited
        
    result = bfs(maps, (0,0)) # y, x
    print(result)
    return result[(len(maps)-1, len(maps[0])-1)] +1 if (len(maps)-1, len(maps[0])-1) in result else -1

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
