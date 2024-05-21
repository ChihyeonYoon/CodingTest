def solution(clothes):
    answer = 1
    table = {t:[] for i,t in clothes}
    
    for i, t in clothes:
        table[t].append(i)
        
    for v in table.values():
        answer *=(len(v)+1)
    
    return answer -1