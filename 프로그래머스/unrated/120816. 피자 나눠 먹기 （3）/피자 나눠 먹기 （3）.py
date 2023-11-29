def solution(slice, n):
    a = int(n/slice)
    return a+1 if a*slice < n else a