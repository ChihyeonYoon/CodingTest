# 50 50 70 80
# XX XX 70 80
# XX XX XX 80
# XX XX XX XX

# 70 50 80 30 -> 30 50 70 80
# XX 50 80 XX    XX 50 XX 80
# XX XX 80 XX    XX 50 XX 80
# XX XX XX XX    XX XX XX XX

def solution(people, limit):
    answer = 0
    l,r = 0, len(people)-1
    
    
    boat = 0
    people.sort()
    # print(people)
    
    gone = set()
    
    while l<r:
        # print(l,r)
#         print(people[l], people[r])
            
        if people[l]+people[r] <= limit:
            # print(f"\t{people[l]}+{people[r]} <= {limit}")
            answer +=1
            gone.add(l)
            gone.add(r)
            l+=1
            r-=1
            
            continue
            
        elif people[l]+people[r] > limit:
            r-=1
        
    # print(gone)
    for i,_ in enumerate(people):
        if i not in gone:
            answer +=1
            
    return answer