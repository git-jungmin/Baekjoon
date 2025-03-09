def solution(clothes):
    answer = 1
    kind = dict()
    for i in clothes:
        if i[1] in kind:
            kind[i[1]] += 1
        else:
            kind[i[1]] = 1
    for i in kind.values():
        answer *= (i + 1)
    return answer - 1