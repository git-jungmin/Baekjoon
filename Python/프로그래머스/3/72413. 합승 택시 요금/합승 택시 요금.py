import heapq
INF = int(1e9)

def dik(start,g,n):
        heap = []
        distance = [INF] * (n + 1)
        heapq.heappush(heap, (0,start))
        distance[start] = 0
        
        while heap:
            dist, node = heapq.heappop(heap)
            
            if dist > distance[node]:
                continue
            
            for next_dist, next_node in g[node]:
                new_dist = dist + next_dist
                
                if distance[next_node] > new_dist:
                    heapq.heappush(heap, (new_dist,next_node))
                    distance[next_node] = new_dist
        
        return distance

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    
    for i,j,f in fares:
        graph[i].append((f,j))
        graph[j].append((f,i))
            
        
    # s > i
    dist_s = dik(s,graph,n)
    # a > i
    dist_a = dik(a,graph,n)
    # b > i
    dist_b = dik(b,graph,n)
    
    min_dist = INF
    
    for i in range(1,n+1):
        min_dist = min(min_dist, dist_s[i] + dist_a[i] + dist_b[i])
    
    return min_dist