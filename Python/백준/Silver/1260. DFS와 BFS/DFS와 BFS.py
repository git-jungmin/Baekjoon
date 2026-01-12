import sys
input = sys.stdin.readline
from collections import deque

N,M,V = map(int,input().split(" "))

gragh = [[] for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int,input().split(" "))
    gragh[n1].append(n2)
    gragh[n2].append(n1)

visited = [False] * (N+1)

def dfs(v):
    visited[v] = True
    print(v,end = " ")

    for i in sorted(gragh[v]):
        if visited[i] == False:
            dfs(i)
    
dfs(V)
print()

visited = [False] * (N+1)

def bfs(v):
    q = deque([v])
    visited[v] = True

    while q:
        node = q.popleft()
        print(node,end = " ")
        for i in sorted(gragh[node]):
            if not visited[i]:
                q.append(i)
                visited[i] = True

bfs(V)