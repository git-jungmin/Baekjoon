from itertools import permutations
def is_prime(n):
    if n < 2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1
def solution(numbers):
    nums = set()
    for i in range(1,8):
        for j in permutations(numbers,i):
            num = int(''.join(j))
            if is_prime(num) == 1:
                nums.add(num)
    return len(nums)