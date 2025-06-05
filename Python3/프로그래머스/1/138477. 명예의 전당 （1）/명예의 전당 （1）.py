def solution(k, score):
    answer = []
    top = []
    for i in score:
        if len(top) < k:
            top.append(i)
        else:
            if min(top) < i:
                top.remove(min(top))
                top.append(i)
        answer.append(min(top))
    return answer