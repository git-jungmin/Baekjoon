import sys
input = sys.stdin.readline

k = int(input())

signs = input().split()
visited = [False] * 10

min_num, max_num = "9999999999", "0"

def check(n1,n2,sign):
    if sign == "<":
        return n1 < n2
    return n1 > n2

def dfs(nums):
    global min_num, max_num

    if len(nums) == k+1:
        if nums > max_num:
             max_num = nums
        if nums < min_num:
            min_num = nums
        return
    
    for i in range(10):
        if not visited[i]:
            if len(nums) == 0 or check(int(nums[-1]),i,signs[len(nums)-1]):
                visited[i] = True
                dfs(nums + str(i))
                visited[i] = False

dfs("")
print(max_num)
print(min_num)