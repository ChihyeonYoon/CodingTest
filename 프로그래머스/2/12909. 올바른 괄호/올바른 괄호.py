def solution(s):
    stack=[]
    for s_ in s:
        if s_ == "(":
            stack.append(s_)
        else:
            if stack:
                stack.pop()
            else:
                return False
        
    if stack:
        return False
    return True