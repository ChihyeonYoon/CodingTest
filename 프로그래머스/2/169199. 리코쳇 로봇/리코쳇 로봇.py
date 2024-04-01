from collections import deque

def solution(board):
    answer = -1
    y_len, x_len = len(board), len(board[0])

    for y, line in enumerate(board):
        for x, w in enumerate(line):
            if w =='R':
                start_y, start_x = y, x

    q = deque([(start_y, start_x, 0)])
    visited = [[False]*x_len for _ in range(y_len)]
    
    direction = [(-1,0), (1,0), (0,1), (0,-1)]

    while q:
        cur_y, cur_x, turn = q.popleft()

        if board[cur_y][cur_x] == "G":
            answer = turn
            break

        for dir in direction:
            dy, dx = dir
            step = 1
            while True:
                next_y, next_x = cur_y+step*dy, cur_x+step*dx
                if not(0<=next_y<y_len) or not(0<=next_x<x_len) or board[next_y][next_x] == 'D':
                    if visited[next_y-dy][next_x-dx] == False:
                        q.append((next_y-dy,next_x-dx,turn+1))
                        visited[next_y-dy][next_x-dx] = True
                    break
                step +=1

    return answer