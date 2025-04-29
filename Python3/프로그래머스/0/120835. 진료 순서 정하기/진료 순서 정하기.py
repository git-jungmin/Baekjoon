def solution(emergency):
    answer = []
    priority = sorted(emergency, reverse = True)
    for j in emergency:
        for i,v in enumerate(priority):
            if v == j:
                answer.append(i+1)
    return answer