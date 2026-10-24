import heapq
INF = int(1e9)

def solution(n, edge):
    gragh = [[] for _ in range(n + 1)]
    for a,b in edge:
        gragh[a].append(b)
        gragh[b].append(a)
    
    # 거리,노드
    queue = []
    visited = [False] * (n + 1)
    heapq.heappush(queue, (0,1))
    distance = [INF] * (n + 1)
    distance[0] = 0
    distance[1] = 0
    
    while queue:
        dist, node = heapq.heappop(queue)
        
        if visited[node]:
            continue
            
        visited[node] = True
        
        for i in gragh[node]:
            tot_dist = dist + 1
            if tot_dist < distance[i]:
                distance[i] = tot_dist
                heapq.heappush(queue, (tot_dist,i))
    
    return distance.count(max(distance))