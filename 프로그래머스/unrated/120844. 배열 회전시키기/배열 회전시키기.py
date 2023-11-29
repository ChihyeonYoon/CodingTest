def solution(numbers, direction):
    if direction == "right":
        x = numbers.pop()
        numbers.insert(0,x)
        
    if direction == "left":
        x = numbers.pop(0)
        numbers.append(x)
    return numbers