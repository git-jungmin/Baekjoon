def solution(n):
    answer = 0
    total = 1
    for i in range(1, 11):
        total *= i
        if total <= n:
            answer = i
    return answer