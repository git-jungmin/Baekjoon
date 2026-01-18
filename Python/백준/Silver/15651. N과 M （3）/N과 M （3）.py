import sys
input = sys.stdin.readline

N,M = map(int, input().split(" "))

selected = []

def dfs():
    if len(selected) == M:
        print(*selected)
        return
    
    for i in range(1, N+1):
        selected.append(i)
        dfs()
        selected.pop()

dfs()