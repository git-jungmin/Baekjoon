def solution(s):
    answer = 0
    a,b = 0,0
    c = ''
    for i in s:
        if not c:
            c = i
            a += 1
        else:
            if i == c:
                a += 1
            else:
                b += 1
        if a == b:
            answer += 1
            c = ''
            a,b = 0,0
    if c:
        answer += 1
    return answer