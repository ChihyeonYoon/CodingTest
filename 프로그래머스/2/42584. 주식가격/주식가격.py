def solution(prices):
    from collections import deque
    answer = []
    prices = deque(prices)

    while prices:
        cnt = 0
        p = prices.popleft()
        for p_ in prices:
            if p > p_:
                cnt+=1
                break
            cnt+=1
        
        answer.append(cnt)

    return answer