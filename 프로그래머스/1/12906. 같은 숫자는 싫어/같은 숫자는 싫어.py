def solution(arr):
    answer = []
    for a in arr:
        if a not in answer or a != answer[-1]:
            answer.append(a)
    return answer