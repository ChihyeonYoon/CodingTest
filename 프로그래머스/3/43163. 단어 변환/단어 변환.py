def solution(begin, target, words):

    def CanChange(s,t):
        diff = 0
        for s_ , t_ in zip(s,t):
            if s_ != t_:
                diff +=1
        if diff == 1:
            return True
        else: return False

    if target not in words:
        return 0

    from collections import deque
    q = deque()
    q.append((begin, 0))

    while q:
        cur, dep = q.popleft()

        if cur == target:
            return dep
        
        for w in words:
            if CanChange(cur,w):
                q.append((w,dep+1))
