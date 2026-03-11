import sys
input = sys.stdin.readline

S = input().strip().split('-')

total = sum(map(int, S[0].split("+")))

for s in S[1:]:
    total -= sum(map(int, s.split("+")))

print(total)