import sys
input = sys.stdin.readline

N,S = map(int, input().split())

arr = list(map(int, input().split(" ")))

answer = 0

def dfs(tot,start):
    global answer

    if start == N:
        if tot == S:
            answer += 1
        return
    
    # 현재 원소 포함
    dfs(tot+arr[start], start+1)
    # 현재 원소 미포함
    dfs(tot, start+1)

# 공집합 제거
if S == 0:
    answer -= 1

dfs(0,0)
print(answer)