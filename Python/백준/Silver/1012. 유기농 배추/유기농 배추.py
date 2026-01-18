import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

# 위, 아래, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque([(x,y)])
    gragh[x][y] = False
    while queue:
        cx,cy = queue.popleft()
        for i in range(4):
            nx,ny = cx+dx[i],cy+dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if gragh[nx][ny]:
                    gragh[nx][ny] = False
                    queue.append((nx,ny))

for t in range(T):
    M,N,K = map(int, input().split(" "))
    gragh = [[False] * M for _ in range(N)]
    
    for i in range(K):
        x,y = map(int, input().split(" "))
        gragh[y][x] = True
    
    count = 0
    for n in range(N):
        for m in range(M):
            if gragh[n][m]:
                bfs(n,m)
                count += 1
    print(count)