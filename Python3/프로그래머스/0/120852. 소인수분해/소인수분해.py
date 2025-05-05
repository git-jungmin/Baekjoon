def solution(n):
    answer = set()
    i = 2
    while i * i <= n:
        if n % i == 0:
            answer.add(i)
            n //= i
        else:
            i += 1
    if n > 1:
        answer.add(n)
    return sorted(list(answer))