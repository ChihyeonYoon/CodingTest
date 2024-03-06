def solution(keymap, targets):
    answer = [-1 for _ in range(len(targets))]
    # all_char = 
    keyboard = {}

    for key in keymap:
        for i, k in enumerate(key):
            if k not in keyboard or keyboard[k]>i:
                keyboard[k]=i+1

    # print(keyboard)

    for i, target in enumerate(targets):
        s = 0
        try:
            for t in target:
                s+=keyboard[t]
            answer[i] = s
        except:
            continue
            
    return answer