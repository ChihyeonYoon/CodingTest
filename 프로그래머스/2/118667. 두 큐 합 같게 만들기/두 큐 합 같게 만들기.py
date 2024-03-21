def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)
    if (sum1 + sum2) % 2 == 1:
        return -1
    
    n = len(queue1)
    l1, l2 = 0, n

    def get_num(idx):
        idx %= 2 * n
        return queue1[idx] if idx<n else queue2[idx-n]
    
    answer = 0
    while sum1 != sum2 and answer <=3*n:
        answer +=1
        if sum1>sum2:
            num = get_num(l1)
            sum1 -= num
            sum2 += num
            l1 +=1
        else:
            num = get_num(l2)
            sum1 += num
            sum2 -= num
            l2 +=1
    
    return answer if answer <= 3*n else -1