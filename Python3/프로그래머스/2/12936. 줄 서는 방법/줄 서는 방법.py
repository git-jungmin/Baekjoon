import math
def solution(n, k):
    fact = 1
    for i in range(2, n):
        fact *= i
    
    nums = list(range(1, n + 1))
    answer = []
    for i in range(n, 0, -1):
        if i == 1:
            answer.append(nums.pop())
            break
        idx = math.ceil(k / fact) - 1
        answer.append(nums.pop(idx))
        k %= fact
        fact //= (i-1)
    
    return answer