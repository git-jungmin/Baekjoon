def solution(n, s):
    if s < n:
        return [-1]
    base = s // n
    rem = s % n
    answer = [base] * n
    for i in range(rem):
        answer[-1-i] += 1
    return answer