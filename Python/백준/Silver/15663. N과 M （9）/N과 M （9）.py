import sys
input = sys.stdin.readline

N,M = map(int,input().split(" "))

arr = sorted(list(map(int,input().split(" "))))

visited = [False] * N

def dfs(selected):
    if len(selected) == M:
        print(*selected)
        return

    prev = 0
    for i in range(N):
        if visited[i] == False and prev != arr[i]:
            visited[i] = True
            selected.append(arr[i])
            prev = arr[i]
            dfs(selected)
            visited[i] = False
            selected.pop()

dfs([])