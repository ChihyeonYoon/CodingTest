def solution(numbers):
    max_ = max(numbers)
    numbers.remove(max_)
    
    max__ = max(numbers)
    numbers.remove(max__)
    return max_*max__