import heapq
def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    heap = [(0, 1)]
    while heap:
        time, node = heapq.heappop(heap)
        for next_node, next_time in graph[node]:
            new_time = time + next_time
            if new_time < dist[next_node]:
                dist[next_node] = new_time
                heapq.heappush(heap,(new_time,next_node))
    return sum(1 for d in dist if d <= K)