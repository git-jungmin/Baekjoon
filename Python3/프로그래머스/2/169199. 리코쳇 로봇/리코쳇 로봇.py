from collections import deque
def solution(board):
    n, m = len(board), len(board[0])
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                sx,sy = i,j
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    visited = [[-1] * m for _ in range(n)]
    queue = deque([(sx,sy)])
    visited[sx][sy] = 0

    while queue:
        x,y = queue.popleft()
        
        if board[x][y] == "G":
            return visited[x][y]

        for i in range(4):
            tx, ty = x, y
            
            while True:
                nx, ny = tx + dx[i], ty + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    break
                
                if board[nx][ny] == 'D':
                    break
                    
                tx, ty = nx, ny
                
            if visited[tx][ty] == -1:
                visited[tx][ty] = visited[x][y] + 1
                queue.append((tx,ty))
            
    return -1