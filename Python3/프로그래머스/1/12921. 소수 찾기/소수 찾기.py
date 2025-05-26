def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
def solution(n):
    return sum(1 for i in range(2,n+1) if is_prime(i))