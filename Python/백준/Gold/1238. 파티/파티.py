# 목적지로 가는 길 최단시간들 중 최대 시간 구하기, 단방향

import sys
import heapq
input = sys.stdin.readline

N,M,X = map(int, input().split())
gragh = [[] for _ in range(N+1)]
regragh = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, time = map(int, input().split())
    gragh[start].append((end, time))
    regragh[end].append((start, time))

# deque : FIFO, heapq : 우선순위 큐(min-heap)
def dik(start, g):
    distance = [int(1e9)] * (N+1)
    queue = []
    heapq.heappush(queue, (start, 0))
    distance[start] = 0

    while queue:
        now, dist = heapq.heappop(queue)

        if distance[now] < dist:
            continue
        
        for next, cost in g[now]:
            new_cost = dist + cost
            if distance[next] > new_cost:
                distance[next] = new_cost
                heapq.heappush(queue, (next, new_cost))
    return distance

# X > i
back = dik(X,gragh)

# i > X
go = dik(X,regragh)

answer = 0
for i in range(1,N+1):
    answer = max(answer, go[i] + back[i])
print(answer)