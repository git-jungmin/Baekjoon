def solution(k, m, score):
    answer = 0
    sort_score = sorted(score, reverse = True)
    for i in range(0, len(sort_score) - m + 1, m):
        box = sort_score[i : i + m]
        answer += min(box) * m
    return answer