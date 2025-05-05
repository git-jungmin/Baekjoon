def solution(n, lost, reserve):
    r = sorted(set(reserve) - set(lost))
    l = sorted(set(lost) - set(reserve))
    answer = n - len(l)
    print(r, l)
    for i in l:
        if i-1 in r:
            r.remove(i-1)
            answer += 1
        elif i+1 in r:
            r.remove(i+1)
            answer += 1
    return answer