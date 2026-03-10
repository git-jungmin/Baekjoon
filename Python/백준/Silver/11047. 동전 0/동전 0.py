import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input().strip()))

total = 0
idx = N - 1
while K > 0:
    if coins[idx] <= K:
        total += K // coins[idx]
        K %= coins[idx]
    idx -= 1

print(total)