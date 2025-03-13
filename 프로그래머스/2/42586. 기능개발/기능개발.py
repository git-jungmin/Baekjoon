import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    deploy_day = days[0]
    count = 0

    for day in days:
        if day > deploy_day:
            answer.append(count)
            deploy_day = day
            count = 1
        else:
            count += 1

    answer.append(count)  # Append the last group
    return answer
