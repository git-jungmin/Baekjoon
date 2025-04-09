def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        row = i // n + 1
        index = i % n + 1
        answer.append(max(row, index))
    return answer