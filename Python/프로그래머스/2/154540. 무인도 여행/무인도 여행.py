from collections import deque
def solution(maps):
    arr = [[0 if word == 'X' else int(word) for word in row] for row in maps]
    
    len_X, len_Y = len(arr), len(arr[0])
    
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    def bfs(x,y):
        queue = deque([(x,y)])
        visited[x][y] = True
        total = 0
        
        while queue:
            cx, cy = queue.popleft()
            total += arr[cx][cy]
            
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if nx < 0 or nx >= len_X or ny < 0 or ny >= len_Y or arr[nx][ny] == 0 or visited[nx][ny]:
                    continue
                queue.append([nx,ny])
                visited[nx][ny] = True
        
        return total
    
    visited = [[False] * len_Y for i in range(len_X)]
    area = []
    for i in range(len_X):
        for j in range(len_Y):
            if arr[i][j] == 0 or visited[i][j]:
                continue
            area.append(bfs(i,j))
            
    return sorted(area) if area else [-1]