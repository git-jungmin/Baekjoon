import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split(" "))

gragh = [list(map(int, input().strip())) for _ in range(N)]

# up, down, left, right
dx = [-1, 1, 0, 0] # 행
dy = [0, 0, -1, 1] # 열

def bfs():
    q = deque()
    q.append((0,0))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if gragh[nx][ny] == 1:
                gragh[nx][ny] = gragh[x][y] + 1
                q.append((nx,ny))
    return gragh[N-1][M-1]

print(bfs())