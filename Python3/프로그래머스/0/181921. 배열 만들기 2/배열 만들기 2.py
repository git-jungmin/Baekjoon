def solution(l, r):
    answer = []
    for i in range(l,r+1):
        r = True
        for j in str(i):
            if j not in ('0','5'):
                r = False
                break
        if r:
            answer.append(i)
    return answer if answer else [-1]