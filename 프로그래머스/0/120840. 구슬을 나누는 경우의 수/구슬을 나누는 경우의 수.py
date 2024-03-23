def solution(balls, share):
    from math import factorial
    return factorial(balls)/(factorial(balls-share)*factorial(share))