import sys
from collections import deque
input = sys.stdin.readline
import copy

N,M = map(int, input().split(" "))

gragh = [list(map(int, input().split(" "))) for _ in range(N)]
virus = []
empty = []

# 위,아래,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    for j in range(M):
        if gragh[i][j] == 2:
            virus.append((i,j))
        elif gragh[i][j] == 0:
            empty.append((i,j))

answer = 0

def bfs():
    global answer
    queue = deque(virus)
    temp = copy.deepcopy(gragh)
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx,ny))
    answer = max(answer, sum(row.count(0) for row in temp))

def dfs(idx,count):
    if count == 3:
        bfs()
        return
    
    if idx == len(empty):
        return
    
    x,y = empty[idx]
    gragh[x][y] = 1
    dfs(idx+1, count+1)
    gragh[x][y] = 0
    dfs(idx+1, count)

dfs(0,0)
print(answer)