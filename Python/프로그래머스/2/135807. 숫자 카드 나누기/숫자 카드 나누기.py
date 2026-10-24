import math
from functools import reduce

def gcd_of_list(arr): # 여러수의 최대공약수
    return reduce(math.gcd, arr)

def get_divisors(n): # 약수 구하기
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

def common_divisors(nums): # 여러 수의 공약수
    g = gcd_of_list(nums)
    return get_divisors(g)

def solution(arrayA, arrayB):
    answer = set()
    for i in common_divisors(arrayA):
        if all(b % i != 0 for b in arrayB):
            answer.add(i)
    for j in common_divisors(arrayB):
        if all(a % j != 0 for a in arrayA):
            answer.add(j)
    return max(answer) if answer else 0