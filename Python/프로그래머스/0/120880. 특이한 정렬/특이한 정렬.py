def solution(numlist, n):
    answer = []
    for i in numlist:
        answer.append([abs(n-i),i])
    return [j[1] for j in sorted(answer, key=lambda x: (x[0], -x[1]))]