import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,2,1,-1,-2]

def bfs(l,cx,cy,tx,ty):
    visited = [[False]*l for _ in range(l)]
    queue = deque([(cx,cy,0)])
    visited[cx][cy] = True

    while queue:
        x,y,move = queue.popleft()
        if x == tx and y == ty:
            return move
        for i in range(8):
            nx,ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < l and ny >= 0 and ny < l:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny,move+1))

testcase = int(input())
answer = []

for _ in range(testcase):
    l = int(input())
    cx,cy = map(int,input().split(" "))
    tx,ty = map(int,input().split(" "))
    answer.append(bfs(l,cx,cy,tx,ty))

for i in answer:
    print(i)