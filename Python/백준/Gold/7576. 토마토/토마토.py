import sys
input = sys.stdin.readline
from collections import deque

# 열,행
M,N = map(int, input().split(" "))

queue = deque()
gragh = [list(map(int, input().split(" "))) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if gragh[i][j] == 1:
            queue.append((i,j))

# 위, 아래, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    cx,cy = queue.popleft()
    for i in range(4):
        nx,ny = cx + dx[i], cy + dy[i]
        if nx >= 0 and ny >= 0 and nx < N and ny < M:
            if gragh[nx][ny] == 0:
                gragh[nx][ny] = gragh[cx][cy] + 1
                queue.append((nx,ny))

answer = 0
for i in range(N):
    for j in range(M):
        if gragh[i][j] == 0:
            print(-1)
            exit(0)
        answer = max(answer, gragh[i][j])

print(answer - 1)