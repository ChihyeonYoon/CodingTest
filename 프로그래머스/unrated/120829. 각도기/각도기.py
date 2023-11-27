def solution(angle):
    if angle in range(1,90):
        return 1
    elif angle == 90:
        return 2
    elif angle in range(91,180):
        return 3
    elif angle == 180:
        return 4