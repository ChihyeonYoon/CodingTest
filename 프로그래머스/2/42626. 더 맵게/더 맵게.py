from heapq import heapify, heappop, heappush
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    k=scoville[0]
    
    while len(scoville)>=2 and scoville[0]<K:
        s1 = heappop(scoville)
        s2 = heappop(scoville)

        k = s1 + (2*s2)
        answer +=1
        heappush(scoville, k)
            
    return answer if k>=K else -1