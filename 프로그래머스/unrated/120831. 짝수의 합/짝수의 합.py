def solution(n):
    # answer = 0
    # for i in range(0,n+2,2):
    #     answer += i
        
    # even = range(0,n+2,2)
    # return sum(even)
    
    answer = 0
    for i in range(1,n+1):
        if(i%2==0):
            answer += i
    return answer