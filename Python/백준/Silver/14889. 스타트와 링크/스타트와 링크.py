import sys
from collections import deque
 
input = sys.stdin.readline

N = int(input())
n = N // 2

nums = [list(map(int, input().split(" "))) for _ in range(N)]
visited = [False] * N

def dfs(idx,cnt):
    if cnt == n:
        start, link = 0, 0
        for i in range(N):
            for j in range(i+1, N):
                if visited[i] and visited[j]:
                    start += nums[i][j] + nums[j][i]
                elif not visited[i] and not visited[j]:
                    link += nums[i][j] + nums[j][i]
        return abs(start - link)

    gap = int(1e9)
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            gap = min(gap, dfs(i+1, cnt+1))
            visited[i] = False
    return gap

print(dfs(0,0))