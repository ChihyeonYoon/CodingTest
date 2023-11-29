def solution(sides):
    max_ = max(sides)
    sides.remove(max_)
    if max_ < sum(sides):
        return 1
    else: return 2
                          