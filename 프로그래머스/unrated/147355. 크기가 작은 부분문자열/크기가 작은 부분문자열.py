def solution(t, p):
    answer = 0
    size = len(p)
    # print(size)
    
    for i in range(len(t)):
        num = t[i:i+size]
        # print(num)
        if len(num) < size:
            break
        if int(num) <= int(p):
            answer +=1
        
    
    return answer