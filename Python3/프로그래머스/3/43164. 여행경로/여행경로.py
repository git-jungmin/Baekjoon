from collections import defaultdict
def solution(tickets):
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    for key in graph:
        graph[key].sort()
    route = []
    def dfs(current):
        while graph[current]:
            next_dst = graph[current].pop(0)
            dfs(next_dst)
        route.append(current)
    dfs("ICN")
    return route[::-1]