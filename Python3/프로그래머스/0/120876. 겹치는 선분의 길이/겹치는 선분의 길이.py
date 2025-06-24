def solution(lines):
    answer = 0
    l = [0] * 201
    for start,end in lines:
        for i in range(start,end):
            l[100 + i] += 1
    for j in l:
        if j >= 2:
            answer += 1
    return answer