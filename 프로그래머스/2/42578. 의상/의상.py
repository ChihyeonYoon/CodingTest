def solution(clothes:list):
    answer = 1
    table = {t:[] for _, t in clothes}

    for c, t in clothes:
        table[t].append(c)
    
    for v in table.values():
        answer *= (len(v) +1)

    return answer -1