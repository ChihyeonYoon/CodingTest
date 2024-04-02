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