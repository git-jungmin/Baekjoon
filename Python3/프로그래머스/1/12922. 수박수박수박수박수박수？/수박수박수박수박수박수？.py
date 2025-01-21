def solution(n):
    c = n // 2
    if n % 2 == 0:
        answer = '수박' * c
    else:
        answer = '수박' * c + "수"
    return answer