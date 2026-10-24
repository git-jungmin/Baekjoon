def solution(i, j, k):
    answer = 0
    for i in range(i, j + 1):
        for j in str(i):
            if str(k) in j:
                answer += 1
    return answer