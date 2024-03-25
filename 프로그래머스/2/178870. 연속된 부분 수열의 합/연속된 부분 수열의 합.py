def solution(sequence,k):
    answer = []
    
    r = 0
    sum = 0


    for l in range(len(sequence)):
        while sum < k and r<len(sequence):
            sum += sequence[r]
            r+=1
        if sum == k and l < r:
            answer.append([l,r-1])
        sum -= sequence[l]
            
    answer = sorted(answer, key=lambda x:x[1]-x[0])

    return answer[0]