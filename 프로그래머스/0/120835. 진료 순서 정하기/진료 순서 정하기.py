def solution(emergency):
    tmp = sorted(emergency,reverse=True)
    tmp = {e:i+1 for i,e in enumerate(tmp)}
    answer=[]
    for e in emergency:
        answer.append(tmp[e])
        
    
    return answer