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

# def solution(phone_book:list):
#     table = {p:True for p in phone_book}

#     for p in phone_book:
#         prepix = ''
#         for n in p:
#             prepix += n
#             if prepix in table and prepix != p:
#                 return False
#     return True

# def solution(phone_book):
#     prefixs = sorted(phone_book)
#     # print(prefixs)
    
#     dict = {}
#     for num in prefixs:
#         if len(num) not in dict:
#             dict[len(num)] = []
#             dict[len(num)].append(num)
#         else:
#             dict[len(num)].append(num)
            
#     # print(dict)
            
#     for prefix in prefixs:
#         for key in dict.keys():
#             if key > len(prefix):
#                 for number in dict[key]:
#                     if number[:len(prefix)] == prefix:
#                         return False         
        
#     return True