def solution(n, lost, reserve):
    answer = 0
    reserve_dict = {}
    for r in reserve:
        if r not in lost:
            reserve_dict[r] = 2
        else :
            reserve_dict[r] = 1
    print(reserve_dict)
    
    # for l in lost:
    for l in range(1,n+1):
        if l in lost:
            if l-1 in reserve_dict and reserve_dict[l-1] ==2:
                reserve_dict[l-1] -= 1
                answer +=1
            elif l+1 in reserve_dict and reserve_dict[l+1] ==2:
                reserve_dict[l+1]-=1
                answer +=1
            elif l in reserve_dict and reserve_dict[l] == 1:
                answer +=1
            else:
                continue
        else:
            answer+=1
    print(reserve_dict)
    # answer +=len(reserve)
            
    
    
            
    return answer