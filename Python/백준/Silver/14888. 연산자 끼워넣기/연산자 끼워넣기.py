import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split(" ")))

# 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)
plus, minus, mul, div = map(int, input().split(" "))

arr = []
idx = 1

def dfs(num, idx, p, m, mu, d ):
    if idx == N:
        arr.append(num)
        return

    if p > 0:
        dfs(num+nums[idx], idx+1, p-1, m, mu, d)
    if m > 0:
        dfs(num-nums[idx], idx+1, p, m-1, mu, d)
    if mu > 0:
        dfs(num*nums[idx], idx+1, p, m, mu-1, d)
    if d > 0:
        if num < 0:
            dfs(-(-num//nums[idx]), idx+1, p, m, mu, d-1)
        else:
            dfs(num//nums[idx], idx+1, p, m, mu, d-1)

dfs(nums[0], idx, plus, minus, mul, div)

print(max(arr))
print(min(arr))