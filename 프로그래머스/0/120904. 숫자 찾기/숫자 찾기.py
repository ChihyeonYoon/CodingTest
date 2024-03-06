def solution(num, k):
    num=str(num)
    k=str(k)
    for i, n in enumerate(num):
        if n == k:
            return i+1
    return -1
    