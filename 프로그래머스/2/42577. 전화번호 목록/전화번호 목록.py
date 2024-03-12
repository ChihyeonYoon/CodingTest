# def solution(phone_book:list):
#     phone_book.sort(key=lambda x: len(x))
#     # table = {t:True for t in phone_book}
#     from collections import deque
#     phone_book = deque(phone_book)
#     while phone_book:
#         p = phone_book.popleft()
#         if any(t.startswith(p) and t!= p for t in phone_book):
#             return False
#     return True

def solution(phone_book:list):
    table = {p:True for p in phone_book}

    for p in phone_book:
        prepix = ''
        for n in p:
            prepix += n
            if prepix in table and prepix != p:
                return False
    return True
