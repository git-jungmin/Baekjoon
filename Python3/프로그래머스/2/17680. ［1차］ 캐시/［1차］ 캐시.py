def solution(cacheSize, cities):
    answer = 0
    cash = []
    for i in cities:
        i = i.lower()
        if cacheSize == 0:
            answer += 5
            continue
        if i in cash:
            answer += 1
            cash.remove(i)
        else:
            if len(cash) >= cacheSize:
                cash.pop(0)
            answer += 5
        cash.append(i)
    return answer