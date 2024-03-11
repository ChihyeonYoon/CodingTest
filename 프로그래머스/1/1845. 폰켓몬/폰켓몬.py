def solution(nums):
    answer = 0
    table = {}
    for n in nums:
        if n not in table:
            table[n] = 1
        else:
            table[n]+=1
    print(table)
    for t in table:
        if table[t] >=1 and answer < len(nums)//2:
            answer+=1
    return answer