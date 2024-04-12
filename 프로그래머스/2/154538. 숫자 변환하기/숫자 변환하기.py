from collections import deque
def solution(x, y, n):
    answer = 0
    
    if x == y:
        return 0
    
    def bfs(x):
        q = deque([(x,0)])
        visited = {x:0}
        while q:
            cur_x, cur_depth = q.popleft()

            if cur_x == y:
                return cur_depth
            # if cur_x+n >= 1000000:
            #     return -1

            nexts = [cur_x+n,cur_x*2,cur_x*3]
            for next in nexts:
                if next == y:
                    return cur_depth+1
                if next not in visited and next <=y:
                    q.append((next, cur_depth+1))
                    visited[next] = cur_depth+1

    answer = bfs(x)

    return answer if answer else -1