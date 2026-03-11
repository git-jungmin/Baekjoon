import sys
input = sys.stdin.readline

N = int(input())

l = []
for _ in range(N):
    l.append(int(input().strip()))

l.sort()

total = 0
for i in range(N):
    total = max(total, l[i] * (N-i))

print(total)