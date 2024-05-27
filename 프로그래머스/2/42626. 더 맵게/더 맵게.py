from heapq import heapify, heappush, heappop
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    
    while scoville[0] < K and len(scoville)>=2:
        f1 = heappop(scoville)
        f2 = heappop(scoville)
        score = f1 + 2*f2
        answer +=1
        
        heappush(scoville, score)

        
    return answer if scoville[0]>=K else -1