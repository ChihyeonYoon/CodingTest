def solution(my_string, n):
    answer=[]
    for s in list(my_string):
        for i in range(0,n):
            answer.append(s)
    return ''.join(answer)