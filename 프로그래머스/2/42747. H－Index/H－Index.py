def solution(citations):
    hindex = 0
    citations.sort(reverse=True)
    for i, citation in enumerate(citations):
        if citation >= i+1:
            hindex=i+1
        else:
            break
    return hindex