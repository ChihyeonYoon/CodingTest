def solution(s):
    
    stack = []
    
    for i in s:
        if i == '(':
            stack.append('(')
            
        if i == ')':
            try:
                stack.pop()
            except:
                return False
        
    if len(stack) == 0 :
        return True
            
    return False