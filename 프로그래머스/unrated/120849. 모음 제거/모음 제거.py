def solution(my_string):
    if 'a' in my_string:
        my_string = my_string.replace('a', '')
    if 'e' in my_string:
        my_string = my_string.replace('e', '')
    if 'i' in my_string:
        my_string = my_string.replace('i', '')
    if 'o' in my_string:
        my_string = my_string.replace('o', '')
    if 'u' in my_string:
        my_string = my_string.replace('u', '')
    return my_string