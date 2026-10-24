def solution(land):
    # land[i][j]는 i번째 행의 j번째 열
    for i in range(1, len(land)):
        for j in range(4):
            # 바로 위 행의 다른 열 중 최댓값을 찾아 현재 위치에 더함
            land[i][j] += max(land[i - 1][k] for k in range(4) if k != j)

    return max(land[-1])  # 마지막 행에서 최댓값이 정답
