def solution(n, times):
    answer = 0
    min_t, max_t = 1, max(times) * n

    while min_t <= max_t:
        mid_t = (min_t+max_t)//2
        people = 0

        for time in times:
            people += mid_t//time

            if people >= n:
                break
        
        if people >= n:
            answer = mid_t
            max_t = mid_t -1
        if people < n:
            min_t = mid_t +1

    return answer