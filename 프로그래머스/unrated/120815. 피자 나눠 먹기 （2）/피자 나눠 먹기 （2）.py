def GCD(a, b):
    while(b>0):
        a, b = b, a%b
    return a

def solution(n):
    # 6과 n의 최소공배수
    LCM = (6*n) // GCD(6,n)
    
    
    return LCM // 6