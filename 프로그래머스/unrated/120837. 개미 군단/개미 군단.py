def solution(hp):
    a, a_ = divmod(hp,5)
    b, b_ = divmod(a_, 3)
    return a+b+b_