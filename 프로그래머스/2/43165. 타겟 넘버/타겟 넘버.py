def solution(numbers, target):
    
    global answer
    answer = 0
    
    def dfs(sum, i):
        global answer

        if sum == target and i == len(numbers):
            answer +=1
            return
        if i==len(numbers):
            return

        dfs(sum + numbers[i], i+1)
        dfs(sum - numbers[i], i+1)

        return

    dfs(0,0)

    return answer 