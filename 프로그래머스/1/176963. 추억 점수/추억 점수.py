def solution(name, yearning, photo):
    answer = []
    name_yearning = {n:y for n, y in zip(name, yearning)}
    
    print(name_yearning)
    for p in photo:
        score = 0
        for n in p:
            if n not in p:
                continue
            elif n in name_yearning.keys():
                score += name_yearning[n]
        answer.append(score)
    
    return answer