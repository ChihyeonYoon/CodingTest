from collections import deque
def solution(s):
    
    q = deque()
    
    for s_ in s:
        if s_ == '(':
            q.append(s_)
        else:
            if q:
                q.popleft()
            else:
                return False
    if not q: 
        return True
    else:
        return False