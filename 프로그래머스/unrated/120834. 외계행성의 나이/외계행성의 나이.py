def solution(age):
    answer=''
    table=['a','b','c','d','e','f','g','h','i','j']
    age_w = [int(x) for x in list(str(age))]
    for w in age_w:
        answer+=table[w]
    return answer