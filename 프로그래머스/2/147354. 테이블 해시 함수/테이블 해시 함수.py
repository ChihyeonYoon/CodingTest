def solution(data, col, row_begin, row_end):
    answer = 0
    
    # tmp_dict = {}
    # for d in data:
    #     if not tmp_dict.get(d[col-1]):
    #         tmp_dict[d[col-1]] = [d]
    #     else:
    #         tmp_dict[d[col-1]].append(d)

    # for k, i in tmp_dict.items():
    #     tmp_dict[k] = sorted(i, reverse=True)

    # new_data = []
    # for k in sorted(tmp_dict.keys()):
    #     new_data+=tmp_dict[k]

    # print(tmp_dict)
    # print(new_data)
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    
    for i in range(row_begin, row_end+1):
        tple = data[i-1]
        tple_v = 0
        for n in tple:
            tple_v += n%i
        answer ^= tple_v

    return answer