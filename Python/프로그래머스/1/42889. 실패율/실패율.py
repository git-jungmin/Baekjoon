def solution(N, stages):
    answer = []
    result = {}
    for i in range(1,N+1):
        a,b = 0,0
        for j in stages:
            if j >= i:
                b += 1
            if j > i:
                a += 1
        if b != 0:
            result[i] = (b-a)/b
        else:
            result[i] = 0
    for z in sorted(result.items(), key = lambda x:(-x[1],x[0])):
        answer.append(z[0])
    return answer