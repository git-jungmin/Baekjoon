def solution(board):
    n = len(board)
    danger = [[0] * n for _ in range(n)]  # 위험 지역 표시용 배열

    # 8방향(상하좌우 + 대각선)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1), ( 0, 0), ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 지뢰가 있는 경우
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        danger[ni][nj] = 1  # 위험 지역으로 표시

    # 안전 지역 개수 세기
    safe_count = 0
    for i in range(n):
        for j in range(n):
            if danger[i][j] == 0:
                safe_count += 1

    return safe_count
