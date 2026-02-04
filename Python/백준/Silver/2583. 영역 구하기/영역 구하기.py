import sys
input = sys.stdin.readline
from collections import deque

# 행, 열, 직사각형 수
M, N, K = map(int, input().split(" "))

rect = [[False] * N for _ in range(M)]

for i in range(K):
    lx,ly,rx,ry = map(int, input().split(" "))
    for j in range(lx,rx):
        for z in range(ly,ry):
            rect[z][j] = True

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    queue = deque([(x,y)])
    rect[y][x] = True
    count = 1

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < N and ny < M and nx >= 0 and ny >= 0:
                if not rect[ny][nx]:
                    queue.append((nx,ny))
                    rect[ny][nx] = True
                    count += 1
    
    return count
    
areas = []
for i in range(M):
    for j in range(N):
        if not rect[i][j]:
            areas.append(bfs(j,i))

print(len(areas))
print(*sorted(areas))