from collections import deque
def bfs(start_point, end_point, maps):
        y_len = len(maps)-1
        x_len = len(maps[0])-1
        direction = [(-1,0),(1,0),(0,-1),(0,1)]

        start_y, start_x = start_point
        q = deque([(start_y, start_x, 0)]) #(y, x, dist)

        visited = {}
        visited[(start_y, start_x)]=0
        # visited_map = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]

        while q:
            cur_y, cur_x, cur_dist = q.popleft()

            if (cur_y, cur_x) == end_point:
                return cur_dist
            # else:
                # visited[(cur_y, cur_x)]=cur_dist
                # visited_map[cur_y][cur_x]=True

            for y, x in direction:
                next_y, next_x = cur_y+y, cur_x+x
                # if 0 <= next_y <= y_len and 0 <= next_x <= x_len and visited_map[next_y][next_x]==False:
                if 0 <= next_y <= y_len and 0 <= next_x <= x_len and (next_y, next_x) not in visited:
                    if maps[next_y][next_x] != 'X':
                        q.append((next_y, next_x, cur_dist+1))
                        visited[(next_y, next_x)]=cur_dist+1

        return None

def solution(maps):
    start_point, lever_point, end_point, flag = None,  None,  None, False

    for y, row in enumerate(maps):
        for x, s in enumerate(row):
            if s == 'S':
                start_point = (y,x)
            if s == 'L':
                lever_point = (y,x)
            if s == 'E':
                end_point = (y,x)
            if start_point and lever_point and end_point:
                flag = True
                break
        if flag:
            break

    dist_s2l = bfs(start_point, lever_point, maps)

    dist_l2e = bfs(lever_point, end_point, maps)

    if dist_s2l == None or dist_l2e == None:
        return -1
    else:
        return dist_s2l+ dist_l2e