import sys
input = sys.stdin.readline

N,D = map(int, input().split())
gragh = [[] for _ in range(D+1)]

# 지름길 정보 저장
for _ in range(N):
    start,end,length = map(int, input().split())
    if end <= D and length < end - start:
        gragh[start].append((end,length))

dp = [i for i in range(D+1)]

# DP 계산
for i in range(D+1):
    if i > 0:
        dp[i] = min(dp[i], dp[i-1]+1)
    for e,l in gragh[i]:
        dp[e] = min(dp[e],l+dp[i])

print(dp[-1])