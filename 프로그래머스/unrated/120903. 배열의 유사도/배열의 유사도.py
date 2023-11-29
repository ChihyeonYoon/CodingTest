def solution(s1, s2):
    answer = 0
    for s in s1:
        for s_ in s2:
            if s == s_ :
                answer += 1
    return answer