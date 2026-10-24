import heapq
def solution(tickets):
    route = []
    graph = dict()
    
    for start, end in tickets:
        if start not in graph:
            graph[start] = []
        
        graph[start].append(end)
    
    for key in graph:
        graph[key].sort()
    
    print(graph)
    
    route = ["ICN"]
    
    def dfs(start):
        if len(tickets) + 1 == len(route):
            return True
    
        if start not in graph:
            return False
        
        for i in range(len(graph[start])):
            next_dest = graph[start][i]
            graph[start].pop(i)
            route.append(next_dest)
            
            if dfs(next_dest):
                return True
            
            route.pop()
            graph[start].insert(i, next_dest)

    dfs("ICN")
    return route
        
        