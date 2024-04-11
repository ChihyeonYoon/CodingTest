from collections import Counter
def solution(weights):
    answer = 0
    counter = Counter(weights)
    # print(counter)

    for _, n in counter.items(): # 같은 무게가 n개 있는 경우 nC2
        if n >= 2:
            answer += (n*(n-1))//2 # combination: n!/((n-r)!r!)

    weights = set(weights)

    # iteration 1 
    for w in weights:
        if w*3/2 in weights: 
            answer+=counter[w*3/2]*counter[w] 
        if w*2 in weights: 
            answer+=counter[w*2]*counter[w] 
        if w*4/3 in weights:
            answer+=counter[w*4/3]*counter[w]

    return answer