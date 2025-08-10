from itertools import chain
def solution(n):
    snail = [[0] * i for i in range(1,n+1)]
    top,bot,thick = 0,n-1,0
    num = 1
    while n > 0:
        for i in range(n):
            snail[top+i][thick] = num
            num += 1
        if n > 2:
            for j in range(n-2): # 횟수
                snail[bot][thick+1+j] = num
                num += 1
        if n > 1:
            for z in range(n-1): # 횟수
                snail[bot-z][-1-thick] = num
                num += 1
        top += 2
        n -= 3
        thick += 1
        bot -= 1
    answer = []
    for _ in snail:
        answer += _
    return answer