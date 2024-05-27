from heapq import heapify, heappush, heappop
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    score=scoville[0]
    
    while scoville[0] < K and len(scoville)>=2:
        f1 = heappop(scoville)
        f2 = heappop(scoville)
        score = f1 + 2*f2
        answer +=1
        
        heappush(scoville, score)

        
    return answer if score>=K else -1