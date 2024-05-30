from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque([(0, -1)]) # sum, level
    while queue:
        s, l = queue.popleft()
        print(f"l: {l}, s: {s}")
        if l > len(numbers):
            break
        
        elif l == len(numbers)-1 and s == target:
            answer += 1

        elif 0<=l+1<len(numbers):
            queue.append((s+numbers[l+1], l+1))
            queue.append((s-numbers[l+1], l+1))

    return answer

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
