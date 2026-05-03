def solution(n, results):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    
    for a,b in results:
        graph[a][b] = 1
        graph[b][a] = -1
        
    for b in range(1,n+1):
        for a in range(1,n+1):
            for c in range(1,n+1):
                if graph[a][b] == 1 and graph[b][c] == 1:
                    graph[a][c] = 1
                    graph[c][a] = -1
    
    answer = 0
    
    for i in range(1,n+1):
        count = 0
        for j in range(1,n+1):
            if graph[i][j] != 0:
                count += 1
        if count == n - 1:
            answer += 1
    
    return answer