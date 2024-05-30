def solution(numbers, target):
    global answer
    answer = 0
    
    def dfs(numbers, idx, v):
        global answer
        
        # print(f"idx: {idx}, v: {v}")
        if v == target and idx == len(numbers)-1:
            # print("collect")
            answer += 1
            return
        
        elif idx+1 <= len(numbers)-1:
            dfs(numbers, idx+1, v+numbers[idx])
            dfs(numbers, idx+1, v-numbers[idx])
    
    dfs(numbers, -1, 0)
    return answer