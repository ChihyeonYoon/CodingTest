def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)
    if (sum1 + sum2) % 2 == 1: # 두 큐의 합이 홀수라면 두 큐에 대한 합을 같게 만들 수 없음
        return -1
    
    n = len(queue1)
    l1, l2 = 0, n # 두 큐가 원형 큐로 이어져있다고 가정, l1: 첫번 째 큐의 0번 인덱스, l2: 두번 째 큐의 0번 인덱스

    def get_num(idx):
        idx %= 2 * n 
        # idx=5, n=4 -> 5%8 = 5    
        # idx=2, n=4 -> 2%8 = 2
        # idx가 원형 큐에서 유지되도록 %=2*n 을 해준다
        return queue1[idx] if idx<n else queue2[idx-n] # 
    
    answer = 0
    while sum1 != sum2 and answer <=3*n: # answer <=3*n: while 문이 최대로 수행되는 횟수, 두 큐가 원형 큐로 연결되어 있다고 가정하면 다시 제자리로 돌아오기 까지 최대 횟수 3n
        answer +=1
        if sum1>sum2: # 첫번 째 큐의 합이 더 큰 경우
            num = get_num(l1)
            sum1 -= num
            sum2 += num
            l1 +=1
        else: # 첫번 째 큐의 합이 더 작은 경우
            num = get_num(l2)
            sum1 += num
            sum2 -= num
            l2 +=1
    
    return answer if answer <= 3*n else -1