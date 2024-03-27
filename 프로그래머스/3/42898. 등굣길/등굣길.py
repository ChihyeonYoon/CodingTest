def solution(m, n, puddles):
    answer = 0

    memo={(n,m):1}
    for puddle in puddles:
        x, y = puddle
        memo[(y,x)] = 0
    
    def dfs(y,x):
        if x == m and y == n:
            return memo[(n,m)]
        
        # if [x,y] in puddles or not (1<=y<=n) or not (1<=x<=m): 
        if not (1<=y<=n) or not (1<=x<=m): 
            return 0
        
        down = dfs(y+1,x) if (y+1,x) not in memo else memo[(y+1,x)]
        right = dfs(y,x+1) if (y,x+1) not in memo else memo[(y,x+1)]

        if (y,x) not in memo:
            memo[(y,x)] = down+right
        
        return memo[(y,x)]
    
    answer = dfs(1,1)
    return answer%1000000007