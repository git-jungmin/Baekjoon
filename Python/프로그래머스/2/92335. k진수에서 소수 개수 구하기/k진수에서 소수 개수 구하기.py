def to_base_k(n,k):
    re = ""
    while n > 0:
        re = str(n % k) + re
        n //= k
    return re

def is_prime(n):
    if n < 2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

def solution(n, k):
    answer = 0
    num = ""
    for i in to_base_k(n,k):
        if i != '0':
            num += i
        else:
            if num != '':
                answer += is_prime(int(num))
                num = ""
    if num != '':
        answer += is_prime(int(num))
    return answer