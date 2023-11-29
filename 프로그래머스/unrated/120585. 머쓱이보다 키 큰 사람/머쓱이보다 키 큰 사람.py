def solution(array, height):
    array_ = [a for a in array if a > height]
    return len(array_)