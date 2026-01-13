import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
E = int(input())

gragh = [[] for _ in range(N+1)]

for _ in range(E):
    n1,n2 = map(int,input().split(" "))
    gragh[n1].append(n2)
    gragh[n2].append(n1)

visited = [False] * (N+1)
queue = deque([1])
visited[1] = True

while queue:
    computer = queue.popleft()
    for i in gragh[computer]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)

print(sum(visited)-1)