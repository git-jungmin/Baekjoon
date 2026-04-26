# MST 최소 스패닝 트리 (모든 정점이 연결되어 있는 최소 가중치 합)

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
gragh = [[] for _ in range(V + 1)]

for _ in range(E):
    a,b,c = map(int, input().split())
    gragh[a].append((b,c))
    gragh[b].append((a,c))

# Dijkstra : 시작점에서 다른 모든 정점까지의 최단 경로
# MST(Prim) : 전체 노드 연결 비용 최소 (노드 중심)
# MST(Cruskal) : 전체 노드 연결 비용 최소 (간선 중심)

def prim(start):
    visited = [False] * (V + 1)
    queue = [(0,start)]
    tot_cost = 0
    
    while queue:
        cost, node = heapq.heappop(queue)

        if visited[node]:
            continue

        visited[node] = True
        tot_cost += cost

        for i in range(len(gragh[node])):
            next_node, next_cost = gragh[node][i]
            if not visited[next_node]:
                heapq.heappush(queue, (next_cost, next_node))
    return tot_cost

print(prim(1))
