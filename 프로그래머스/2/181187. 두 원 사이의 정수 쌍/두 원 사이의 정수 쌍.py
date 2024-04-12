def solution(r1, r2):
    counter = 0
    y_min, y_max = r1, r2
    
    for x in range(0,r2):
        while r2**2 < y_max**2 + x**2:
            y_max -=1
        
        while y_min and r1**2 <= (y_min)**2 + x**2:
            y_min-=1

        counter += y_max-y_min
    
    return counter*4