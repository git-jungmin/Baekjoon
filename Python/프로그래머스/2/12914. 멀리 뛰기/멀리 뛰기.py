def solution(n):
    n1, n2 = 1, 1
    if n == 1:
        return 1
    for i in range(2, n + 1):
        if i == n:
            return (n1 + n2) % 1234567
        n1, n2 = n2, n1 + n2