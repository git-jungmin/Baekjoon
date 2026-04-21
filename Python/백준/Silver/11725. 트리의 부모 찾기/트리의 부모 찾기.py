# 트리의 부모 찾기

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
gragh = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    gragh[a].append(b)
    gragh[b].append(a)

def bfs(start):
    parents = [0] * (N + 1)
    parents[start] = 1
    queue = deque([(start)])

    while queue:
        node = queue.popleft()
        for next in gragh[node]:
            if parents[next] != 0:
                continue
            queue.append(next)
            parents[next] = node
    return parents

for i in bfs(1)[2:]:
    print(i)