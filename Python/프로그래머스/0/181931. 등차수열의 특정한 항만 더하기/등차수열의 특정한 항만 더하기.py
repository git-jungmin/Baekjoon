def solution(a, d, included):
    answer = 0
    for i, b in enumerate(included):
        if b:
            answer += a + i * d
    return answer