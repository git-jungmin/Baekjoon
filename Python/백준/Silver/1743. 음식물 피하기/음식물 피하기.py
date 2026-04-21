# 가장 큰 음식물 피하기

import sys
from collections import deque
input = sys.stdin.readline

N,M,K = map(int, input().split())
food = [list(map(int,input().split())) for _ in range(K)]

# 상 좌 하 우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[False] * (M+1) for _ in range(N+1)]
size = []

def bfs(x,y):
    if visited[x][y]:
        return

    visited[x][y] = True
    queue = deque([(x,y)])
    count = 1
    while queue:
        cx,cy = queue.popleft()
        for i in range(4):
            nx,ny = cx + dx[i], cy + dy[i]
            if nx < 1 or nx > N or ny < 1 or ny > M:
                continue
            if [nx, ny] in food and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny))
                count += 1
    size.append(count)

for x,y in food:
    bfs(x,y)

print(max(size))