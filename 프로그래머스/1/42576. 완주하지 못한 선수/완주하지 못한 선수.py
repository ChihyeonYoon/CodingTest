def solution(participant:list, completion:list):
    def to_table(l:list):
        table = {x:0 for x in l}
        for x in l:
            if x in table:
                table[x]+=1
        return table

    participant = to_table(participant)
    completion = to_table(completion)


    for p in participant:
        if p not in completion or completion[p] != participant[p]:
            return p