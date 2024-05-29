def solution(brown, yellow):
    answer = []
    carpet_size = brown+yellow
    pair_diff = carpet_size - 1
    
    
    for d in range(2, carpet_size-1):
        t, r = divmod(carpet_size,d)
        # print(d,t,r)
        
        if r == 0:
            pair = [max(d,t),min(d,t)]
            y_region = [max(d,t)-1,min(d,t)-1]
            if (max(d,t)-2)*(min(d,t)-2) == yellow:
                return pair
    
