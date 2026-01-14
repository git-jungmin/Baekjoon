import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [list(map(int,input().strip())) for _ in range(N)]
visited = [[False] *  N for _ in range(N)]

# 방향 벡터 (위,아래,왼쪽,오른쪽)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
    queue = deque()
    count = 1
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        cx,cy = queue.popleft()
        for i in range(4):
            nx,ny = cx + dx[i], cy + dy[i]
            if nx >= 0 and ny >= 0 and nx < N and ny < N:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    count += 1
    return count

complexes = []

for i in range(N): # 행
    for j in range(N): # 열
        if graph[i][j] == 1 and not visited[i][j]:
            complexes.append(bfs(i,j))

print(len(complexes))
complexes.sort()
for c in complexes:
    print(c)