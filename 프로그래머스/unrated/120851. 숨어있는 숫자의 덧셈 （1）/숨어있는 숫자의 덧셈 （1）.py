def solution(my_string):
    sum=0
    for s in my_string:
        try: sum+=int(s)
        except: pass
    return sum