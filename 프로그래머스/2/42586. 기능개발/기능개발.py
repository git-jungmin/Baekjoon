def solution(progresses, speeds):
    answer = []
    days = list(map(lambda x, y: (100 - x) // y if (100 - x) // y == (100 - x) / y else (100 - x) // y + 1 ,progresses, speeds))
    for i in days:
        if len(answer) == 0:
            answer.append(1)
        elif days[sum(answer) - 1] >= i:
            answer[len(answer)] += 1
        else:
            answer.append(1)
    return answer