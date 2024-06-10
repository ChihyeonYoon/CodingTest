def solution(people, limit):
    answer = 0
    # L        H
    people.sort()
    Lidx, Hidx = 0, len(people)-1
    while Lidx < Hidx:
        # 2 go (H + L)
        if people[Lidx] + people[Hidx] <= limit:
            Lidx +=1
            Hidx -=1
        # 1 go (H)
        else:
            Hidx -=1
        answer +=1
    if Hidx == Lidx:
        answer +=1
    return answer

def solution(people, limit):
    answer = 0
    l,r = 0, len(people)-1
    
    boat = 0
    people.sort()
    
    gone = set()
    
    while l<r:
        if people[l]+people[r] <= limit:
            answer +=1
            gone.add(l)
            gone.add(r)
            l+=1
            r-=1
            
            continue
            
        elif people[l]+people[r] > limit:
            r-=1
        
    for i,_ in enumerate(people):
        if i not in gone:
            answer +=1
            
    return answer