from collections import deque
def solution(maps):
    n,m = len(maps),  len(maps[0])
    visited = [[False] * m  for _ in range(n)]
    
    queue = deque()
    queue.append([0,0,1])
    visited[0][0] = True

    direction = [[0,1],[0,-1],[1,0],[-1,0]]
    
    while queue:
        x, y, dist = queue.popleft()
        if x == n - 1 and y == m - 1:
            return dist
        for i in direction:
            nx = x + i[0]
            ny = y + i[1]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx,ny,dist+1])
    return -1