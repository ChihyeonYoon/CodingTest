from collections import deque

def solution(land):
    y_len, x_len = len(land), len(land[0])
    visited = [[False]*x_len for _ in range(y_len)]

    oils = [0]*x_len
    def bfs(y,x):
        q = deque([(y,x)])
        visited[y][x] = True
        
        oil_cnt = 1
        oil_loc = {x}
        
        direction = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            cur_y, cur_x = q.popleft()
            
            for dir in direction:
                dy, dx = dir
                next_y, next_x = cur_y+dy, cur_x+dx

                if 0<=next_y<y_len and 0<=next_x<x_len and not visited[next_y][next_x]:
                    if land[next_y][next_x] == 1:
                        visited[next_y][next_x] = True
                        q.append((next_y, next_x))
                        oil_loc.add(next_x)
                        oil_cnt+=1
        
        for loc in oil_loc:
            oils[loc] += oil_cnt

    for x in range(x_len):
        for y in range(y_len):
            if land[y][x] and not visited[y][x]:
                bfs(y,x)

    return max(oils)

print(solution([[0, 0, 0, 0, 1, 1, 1, 0], 
                [0, 0, 0, 0, 1, 1, 0, 0], 
                [1, 1, 0, 0, 0, 1, 1, 0], 
                [1, 1, 1, 0, 0, 0, 0, 0], 
                [1, 1, 1, 0, 0, 0, 1, 1]]))