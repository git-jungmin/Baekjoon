def solution(n):
    to_base_3 = ''
    while n > 0:
        to_base_3 += str(n%3)
        n //= 3
    return int(to_base_3, 3)