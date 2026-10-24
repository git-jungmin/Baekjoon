def solution(n):
    answer = 0
    for i in range(1, n + 1):
        tot = 0
        for j in range(i, n + 1):
            tot += j
            if tot == n:
                answer += 1
            elif tot > n:
                break
    return answer