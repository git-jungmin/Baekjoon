import math
def solution(progresses, speeds):
    answer = []
    days = list(math.ceil((100 - i) / j) for i, j in zip(progresses, speeds))
    count = 0
    header = days[0]
    for i in days:
        if i <= header:
            count += 1
        else:
            header = i
            answer.append(count)
            count = 1
    answer.append(count)
    return answer