def solution(array, n):
    answer = 0
    d = 0
    for i in array:
        if not answer or max(n,i) - min(n,i) <= d:
            if d == max(n,i) - min(n,i):
                answer = min(answer,i)
            else:
                answer = i
            d = max(n,i) - min(n,i)
    return answer