def solution(n):
    answer = [n]
    while n != 1:
        if n % 2 == 0:
            answer.append(n//2)
            n //= 2
        else:
            answer.append(n * 3 + 1)
            n = n * 3 + 1
    return answer