# 해킹 컴퓨터 개수와 걸리는 시간 구하기
import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

T = int(input())

def dik(gragh, n, start):
    time = [INF] * (n + 1)
    time[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        cost, node = heapq.heappop(queue)

        if cost > time[node]:
            continue

        for next_node, next_cost in gragh[node]:
            new_cost = cost + next_cost
            if new_cost < time[next_node]:
                time[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))

    count = 0
    max_time = 0
    for i in range(1, n + 1):
        if time[i] != INF:
            count += 1
            max_time = max(max_time, time[i])
    
    print(count, max_time)

for i in range(T):
    n, d, c = map(int, input().split())
    gragh = [[] for _ in range(n + 1)]

    for j in range(d):
        a, b, s = map(int, input().split())
        gragh[b].append((a, s))
    
    dik(gragh, n, c)