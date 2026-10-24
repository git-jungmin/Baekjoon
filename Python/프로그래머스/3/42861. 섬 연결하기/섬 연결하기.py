import heapq
def solution(n, costs):
    graph = [[] for _ in range(n)]
    
    for s,e,c in costs:
        graph[s].append((c,e))
        graph[e].append((c,s))
        
    heap = [(0,0)]
    visited = [False] * n
    total_cost = 0
    
    while heap:
        cost, node = heapq.heappop(heap)
        
        if visited[node]:
            continue
        
        visited[node] = True
        total_cost += cost

        for next_cost, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(heap,(next_cost, next_node))
        
    return total_cost