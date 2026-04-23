# 안전지역 최대 개수 구하기
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 상 좌 하 우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(height):
    visited = [[False] * (N) for _ in range(N)]
    count = 0
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] > height and not visited[i][j]:
                count += 1
                visited[i][j] = True
                queue = deque([(i,j)])
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] > height and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
    
    return count

answer = 0
for i in range(0,101):
    count = bfs(i)
    answer = max(answer, count)
print(answer)