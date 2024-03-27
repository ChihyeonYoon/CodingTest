def solution(triangle):
    answer = 0
    
    bottom = len(triangle)-1
    memo={(bottom,idx):triangle[bottom][idx] for idx in range(len(triangle[bottom]))}
     
    def dfs(level, idx):
        if level == bottom:
            # return triangle[level][idx]
            return memo[level][idx]
        
        left = dfs(level+1, idx) if (level+1,idx) not in memo else memo[(level+1,idx)]
        right = dfs(level+1, idx+1) if (level+1,idx+1) not in memo else memo[(level+1,idx+1)]

        if (level,idx) not in memo:
            memo[(level,idx)] = triangle[level][idx]+max(left,right)
        
        return memo[(level,idx)]
    
    answer = dfs(0,0)
    
    return answer