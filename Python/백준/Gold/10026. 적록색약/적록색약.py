import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

board = [list(input().strip()) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,v,b):
    queue = deque([(x,y)])
    v[x][y] = True
    color = b[x][y]

    while queue:
        cx,cy = queue.popleft()
        for i in range(4):
            nx,ny = cx + dx[i], cy + dy[i]
            if nx >= 0 and ny >= 0 and nx < N and ny < N:
                if not v[nx][ny] and b[nx][ny] == color:
                    queue.append((nx,ny))
                    v[nx][ny] = True
    
    return 1

# 일반
normal = 0
visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j,visited,board)
            normal += 1

# 색약
count = 0
color_visited = [[False] * N for _ in range(N)]
color_board = [['G' if c == 'R' else c for c in row] for row in board]

for i in range(N):
    for j in range(N):
        if not color_visited[i][j]:
            bfs(i,j,color_visited,color_board)
            count += 1

print(normal,count)