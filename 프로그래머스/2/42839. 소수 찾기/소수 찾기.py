from itertools import permutations
def solution(numbers):
    
    def is_prime(x):
        for i in range (2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    answers = set()
    permuts = set()
    for len_ in range(1,len(numbers)+1):
        permuts= permuts | set(permutations(numbers,len_))
    
    print(permuts)
    permuts = set(int(''.join(p)) for p in permuts)
    
    print(permuts)
        
    for n in permuts:
        if is_prime(n) and n>1:
            print(n)
            answers.add(n)

    print(answers)
    return len(answers)