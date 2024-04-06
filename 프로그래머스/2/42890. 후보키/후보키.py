from itertools import combinations
def solution(relation):
    # answer = 0
    columns = len(relation[0])
    rows = len(relation)

    answers = []

    for i in range(1,columns+1):
        candidates = list(combinations(range(columns),i))
        # print(candidates)

        for candidate in candidates:
            tples = []
            for row in relation:
                tple =[]
                for idx in candidate:
                    tple.append(row[idx])
                
                if tple not in tples:
                    tples.append(tple)
            
            if len(tples) == rows:
                # print(set(candidate))
                # print("\t",tples,"\n")
                answers.append(set(candidate))

    # print(answers)
    from collections import deque
    answers = deque(answers)
    len_answers = len(answers)  

    answers_ = answers.copy()
    
    for i in range(len(answers)):
        for j in range(i+1,len(answers)):
            key1 = answers[i]
            key2 = answers[j]
            if key1.issubset(key2):
                try:
                    answers_.remove(key2)
                except:
                    continue

    # print(answers_)




    return len(answers_)