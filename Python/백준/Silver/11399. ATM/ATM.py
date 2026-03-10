import sys
input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))

sorted_times = sorted(times)

total = 0
for i in range(1,N+1):
    for j in range(0,i):
        total += sorted_times[j]

print(total)