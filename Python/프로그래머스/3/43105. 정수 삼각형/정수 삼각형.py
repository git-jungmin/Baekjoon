def solution(triangle):
    dq1 = triangle[len(triangle)-1]
    for i in range(len(triangle)-2,-1,-1): # 다른 레벨
        dq2 = []
        for j in range(0,len(triangle[i])): # 같은 레벨
            dq2.append(triangle[i][j] + max(dq1[j],dq1[j+1]))
        dq1 = dq2
    return dq1[0]