def solution(name):
    n = len(name)
    answer = 0
    
    # 상하 이동 횟수 계산
    for char in name:
        # 각 문자에 대해 'A'로 맞추기 위해 필요한 상하 이동 횟수 계산
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    # 좌우 이동 횟수 계산
    min_move = n - 1
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        # 현재 위치까지 이동 후 돌아오는 거리와 비교
        distance = min(i, n - next_idx)
        min_move = min(min_move, i + n - next_idx + distance)
    
    answer += min_move
    return answer

# AABAAABAA
# 2
# i  0
#         next_idx:  2
#         n - next_idx = 9 - 2 = 7
#         distance = min(i, n - next_idx) = min(0, 9 - 2) = 0
#         min_move = min(min_move, i + n - next_idx + distance) = min(8, 0 + 9 - 2 + 0) = 7
# i  1
#         next_idx:  2
#         n - next_idx = 9 - 2 = 7
#         distance = min(i, n - next_idx) = min(1, 9 - 2) = 1
#         min_move = min(min_move, i + n - next_idx + distance) = min(7, 1 + 9 - 2 + 1) = 7
# i  2
#         next_idx:  6
#         n - next_idx = 9 - 6 = 3
#         distance = min(i, n - next_idx) = min(2, 9 - 6) = 2
#         min_move = min(min_move, i + n - next_idx + distance) = min(7, 2 + 9 - 6 + 2) = 7
# i  3
#         next_idx:  6
#         n - next_idx = 9 - 6 = 3
#         distance = min(i, n - next_idx) = min(3, 9 - 6) = 3
#         min_move = min(min_move, i + n - next_idx + distance) = min(7, 3 + 9 - 6 + 3) = 7
# i  4
#         next_idx:  6
#         n - next_idx = 9 - 6 = 3
#         distance = min(i, n - next_idx) = min(4, 9 - 6) = 3
#         min_move = min(min_move, i + n - next_idx + distance) = min(7, 4 + 9 - 6 + 3) = 7
# i  5
#         next_idx:  6
#         n - next_idx = 9 - 6 = 3
#         distance = min(i, n - next_idx) = min(5, 9 - 6) = 3
#         min_move = min(min_move, i + n - next_idx + distance) = min(7, 5 + 9 - 6 + 3) = 7
# i  6
#         next_idx:  9
#         n - next_idx = 9 - 9 = 0
#         distance = min(i, n - next_idx) = min(6, 9 - 9) = 0
#         min_move = min(min_move, i + n - next_idx + distance) = min(7, 6 + 9 - 9 + 0) = 6
# i  7
#         next_idx:  9
#         n - next_idx = 9 - 9 = 0
#         distance = min(i, n - next_idx) = min(7, 9 - 9) = 0
#         min_move = min(min_move, i + n - next_idx + distance) = min(6, 7 + 9 - 9 + 0) = 6
# i  8
#         next_idx:  9
#         n - next_idx = 9 - 9 = 0
#         distance = min(i, n - next_idx) = min(8, 9 - 9) = 0
#         min_move = min(min_move, i + n - next_idx + distance) = min(6, 8 + 9 - 9 + 0) = 6
# 8
