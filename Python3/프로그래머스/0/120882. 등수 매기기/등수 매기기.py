def solution(score):
    avg = [(e + m) / 2 for e, m in score]
    sorted_avg = sorted(avg, reverse=True)
    answer = [sorted_avg.index(a) + 1 for a in avg]
    return answer