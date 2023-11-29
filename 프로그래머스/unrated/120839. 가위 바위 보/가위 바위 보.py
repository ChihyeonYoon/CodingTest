def solution(rsp):
    answer=[]
    for x in rsp:
        if x == '2':
            answer.append('0')
        if x == '0':
            answer.append('5')
        if x == '5':
            answer.append('2')
    return ''.join(answer)