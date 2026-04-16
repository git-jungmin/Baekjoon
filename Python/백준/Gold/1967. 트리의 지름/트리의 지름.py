# 트리의 지름 구하기
# 에러 사항 : 런타임에러
# 에러 이유 : 재귀 깊이 초과
# 에러 해결 방법 : sys.setrecursionlimit() 함수를 이용하여 재귀 깊이 제한을 늘려준다. or bfs로 풀이한다.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]

for i in range(N-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child,weight))
    tree[child].append((parent,weight))

def dfs(node,dist):
    for next_node, weight in tree[node]:
        if visited[next_node] == -1:
            visited[next_node] = dist + weight
            dfs(next_node, dist + weight)

visited = [-1] * (N+1)
visited[1] = 0
dfs(1,0)

far_node = visited.index(max(visited))

visited = [-1] * (N+1)
visited[far_node] = 0
dfs(far_node,0)

print(max(visited))