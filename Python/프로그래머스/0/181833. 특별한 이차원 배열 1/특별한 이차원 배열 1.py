def solution(n):
    answer = []
    for i in range(0,n):
        row = [0] * n
        row[i] = 1
        answer.append(row)
    return answer
            