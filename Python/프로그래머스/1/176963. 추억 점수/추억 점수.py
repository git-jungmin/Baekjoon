def solution(name, yearning, photo):
    answer = []
    for v in photo:
        tot = 0
        for n,y in zip(name, yearning):
            if n in v:
                tot += y
        answer.append(tot)
    return answer