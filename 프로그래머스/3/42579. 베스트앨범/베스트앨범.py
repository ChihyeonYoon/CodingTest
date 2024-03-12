def solution(genres, plays):
    answer = []

    i_g_p = [(i,g,p) for i, (g, p) in enumerate(zip(genres,plays))]
    i_g_p.sort(key=lambda x: x[2], reverse= True)

    table = {}
    table_ = {}
    table_oder =[]
    for i, g, p in i_g_p:
        if g not in table:
            table[g] = [i]
            table_[g] = p
            
        elif g in table and len(table[g])<2:
            table[g].append(i)
            table_[g] += p
        
        else:
            table_[g] += p

    for k, i in table_.items():
        table_oder.append((k,i))
    
    table_oder.sort(key=lambda x: x[1],reverse=True)

    for t, p in table_oder:
        answer += table[t]

    return answer