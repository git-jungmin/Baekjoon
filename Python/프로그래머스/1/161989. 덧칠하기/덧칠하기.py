def solution(n, m, section):
    answer = 0
    start, end = 0,0
    for i in section:
        if i > end:
            answer += 1
            start, end = i, i+m-1
    return answer