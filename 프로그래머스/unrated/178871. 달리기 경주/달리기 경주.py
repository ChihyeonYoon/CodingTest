def solution(players, callings):

    dic = {player : i for i, player in enumerate(players)}

    for c in callings:
        index = dic[c]
        dic[players[index]] = dic[players[index]] - 1
        dic[players[index-1]] = dic[players[index-1]] + 1
        players[index-1], players[index] = players[index], players[index-1]
    return players