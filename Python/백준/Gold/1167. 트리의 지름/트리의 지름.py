# 트리의 지름

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V = int((input()))
gragh = [[] for _ in range(V+1)]

for _ in range(V):
    data = list(map(int, input().split()))[:-1]
    for i in range(1,len(data),2): 
        gragh[data[0]].append((data[i], data[i+1]))

def dfs(node, dist):
    max_node = node
    max_dist = dist
    for (n,w) in gragh[node]:
        if visited[n]:
            continue
        visited[n] = True
        next = dfs(n, dist+w)
        if next[1] > max_dist:
            max_node = next[0]
            max_dist = next[1]
        visited[n] = False
    return max_node, max_dist

visited = [False] * (V+1)
visited[1] = True
node1, dist1 = dfs(1,0)

visited = [False] * (V+1)
visited[node1] = True
node2, dist2 = dfs(node1,0)
print(dist2)