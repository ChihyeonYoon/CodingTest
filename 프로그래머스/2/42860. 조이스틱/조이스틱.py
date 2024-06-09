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

# 예시 입력
print(solution("JEROEN"))  # 56
print(solution("JAN"))     # 23
