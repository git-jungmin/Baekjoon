def solution(d, budget):
    answer = 0
    rest = budget
    d_sort = sorted(d)
    for i in d_sort:
        if rest - i >= 0:
            rest -= i
            answer += 1
    return answer