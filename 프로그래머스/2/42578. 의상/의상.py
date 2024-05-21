def solution(clothes):
    answer = 1
    table = {t:[] for c,t in clothes}
    
    for c, t in clothes:
        table[t].append(c)
    
    print(table)
    
    for v in table.values():
        answer *=(len(v)+1) # len(v)+1 : 해당 종류의 옷을 선택 안하는 경우를 추가
    
    return answer -1 # 아무거도 안입는 경우의 수를 빼줌