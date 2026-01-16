import sys
input = sys.stdin.readline

N,M = map(int, input().split(" "))

# 0:빈칸, 1:집, 2:치킨집

chicken = []
house = []

for i in range(N):
    line = list(map(int, input().split(" ")))
    for j in range(N):
        if line[j] == 1:
            house.append((i,j))
        elif line[j] == 2:
            chicken.append((i,j))
    
visited = []

def dfs(start,cnt):
    answer = int(1e9)
    if cnt == M:
        total = 0
        for hx,hy in house:
            dist = int(1e9)
            for cx,cy in visited:
                dist = min(dist, abs(hx-cx)+abs(hy-cy))
            total += dist
        return total

    for i in range(start, len(chicken)):
        visited.append(chicken[i])
        answer = min(answer, dfs(i+1,cnt+1))
        visited.pop()
    
    return answer

print(dfs(0,0))