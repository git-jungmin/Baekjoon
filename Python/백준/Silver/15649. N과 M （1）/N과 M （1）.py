import sys
input = sys.stdin.readline

N,M  = map(int,input().split(" "))

arr = []
visited = [False] * (N+1)

def dfs():
    if (len(arr) == M):
        print(*arr)
        return
    
    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)

            dfs()
            
            arr.pop()
            visited[i] = False

dfs()