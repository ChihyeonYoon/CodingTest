from collections import deque

def solution(land):
    answer = []
    x_len = len(land[0]) 
    y_len = len(land)
    
    visited=[[False]*x_len for _ in range(y_len)]
    oil=[0]*x_len

    def bfs(y,x):
        q=deque([(y,x)])
        visited[y][x] = True

        cnt=1

        oil_coverd={x}

        directions=[(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            cur_y, cur_x = q.popleft()

            for direction in directions:
                dy, dx = direction
                next_y, next_x = cur_y+dy, cur_x+dx

                if 0<=next_y<=y_len-1 and 0<=next_x<=x_len-1 and visited[next_y][next_x] == False:
                    if land[next_y][next_x] == 1:
                        q.append((next_y, next_x))
                        visited[next_y][next_x] = True
                        oil_coverd.add(next_x) # 방문한 포인트의 x 값들을 set에 추가
                        cnt+=1 # bfs 한번에 얻을 수 있는 oil의 양
        
        for c in oil_coverd:
            oil[c] += cnt # 방문한 x포인트에 bfs로 얻은 oil 값 더해줌

        return # 결과적으로 bfs로 방문한 포인트의 x에 대해 oil양을 얻을 수 있음
        
    
    for x in range(x_len):
        for y in range(y_len):
           
            if land[y][x] == 1 and visited[y][x]==False:
                bfs(y,x)

    return max(oil)