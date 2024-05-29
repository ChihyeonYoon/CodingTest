def solution(answers):
    answer = []
    
    #a = [1, 2, 3, 4, 5]
    #a = [1, 3, 2, 4, 2]
    
    n1 = [1, 2, 3, 4, 5] * 2000# 5 2
    n2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250 # 0 2
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000 # 0 2
    
    cnt1, cnt2, cnt3 = 0, 0, 0
    
    for i in range(10000):
        try:
            if answers[i] == n1[i]:
                cnt1 += 1
            if answers[i] == n2[i]:
                cnt2 += 1
            if answers[i] == n3[i]:
                cnt3 += 1
        except:
            break
    
    mxv = max(cnt1,cnt2,cnt3)
    rank = [[1,cnt1],[2,cnt2],[3,cnt3]]
    rank.sort(key=lambda x:x[1])
    
    for v in rank:
        if v[1] == mxv:
            answer.append(v[0])
            
    answer.sort()
    
    return answer