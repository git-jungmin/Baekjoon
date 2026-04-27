# 두 노드 사이 거리 구하기

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
gragh = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, r = map(int, input().split())
    gragh[a].append((b,r))
    gragh[b].append((a,r))

def bfs(tree, start, end):
    queue = deque([(0,start)])
    visited = [False] * (N+1)
    visited[start] = True
    dist = 0

    while queue:
        cost, node = queue.popleft()

        if node == end:
            return cost
        
        for next_node, next_cost in tree[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((cost + next_cost, next_node))

distance = []

for i in range(M):
    a, b = map(int, input().split())
    distance.append(bfs(gragh,a,b))

print('\n'.join(map(str, distance)))