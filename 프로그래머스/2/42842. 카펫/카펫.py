def solution(brown, yellow):
    carpet_size = brown+yellow
      
    for d in range(2, carpet_size-1):
        t, r = divmod(carpet_size,d)
        
        if r == 0:
            pair = [max(d,t),min(d,t)]
            if (max(d,t)-2)*(min(d,t)-2) == yellow:
                return pair
    
