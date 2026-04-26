# 범위 내의 최대 아이템 개수 구하기 (양방향)

import sys
import heapq
input = sys.stdin.readline

n,m,r = map(int, input().split())
items = list(map(int, input().split()))
gragh = [[] for _  in range(n+1)]

for i in range(r):
    a, b, w = map(int, input().split())
    gragh[a].append((b,w))
    gragh[b].append((a,w))

def dik(start):
    queue = []
    visited = [False] * (n+1)
    count = 0
    heapq.heappush(queue, (0, start))

    while queue:
        cur_w, cur_v = heapq.heappop(queue)
        if visited[cur_v]:
            continue
        visited[cur_v] = True
        count += items[cur_v-1]
        for i in range(len(gragh[cur_v])):
            next_v, next_w = gragh[cur_v][i]
            tot_w = next_w + cur_w
            if not visited[next_v] and tot_w <= m:
                heapq.heappush(queue, (tot_w, next_v))
    return count

answer = 0
for i in range(1, n+1):
    answer = max(answer, dik(i))
print(answer)