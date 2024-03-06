def solution(priorities, location):
    answer = 0
    
    priorities = [(p,i) for i, p in enumerate(priorities)]
    print(priorities)

    while priorities:
        mp = max([p for p,_ in priorities])
        
        while priorities[0][0] != mp:
            tmp = priorities.pop(0)
            priorities.append(tmp)
        
        if priorities[0][0] == mp:
            p, l = priorities.pop(0)
            answer += 1
            if l == location:
                break

    return answer
