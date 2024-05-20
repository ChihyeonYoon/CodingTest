def solution(phone_book:list):
    # table = {p:True for p in phone_book}
    s = set()
    phone_book.sort()
    for p in phone_book:
        prefix = ''
        for n in p:
            prefix += n
            if s.__contains__(prefix):
                return False
        s.add(p)
    return True
