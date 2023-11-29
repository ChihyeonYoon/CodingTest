def solution(n):
    a,b = divmod(n,7)
    if a*7 < n:
        return a+1
    else:
        return a