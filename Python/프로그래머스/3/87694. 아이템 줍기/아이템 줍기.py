# 두배 확장 해야됨!!

from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for _ in range(102)]
    
    # 사각형 채우기
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                board[i][j] = 1
    
    # 내부 제거
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                board[i][j] = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    queue = deque([(characterX*2,characterY*2,0)])
    visited = [[False] * 102 for _ in range(102)]
    
    while queue:
        x, y, d = queue.popleft()
        
        if (x, y) == (itemX*2, itemY*2):
            return d // 2
            
        visited[x][y] = True
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if board[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny, d + 1))