def solution(m, n, puddles):
    dq = [[0] * (m+1) for i in range(n+1)]
    dq[1][1] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i == 1 and j == 1:
                continue
            if [i,j] not in puddles:
                dq[j][i] = dq[j-1][i] + dq[j][i-1]
    return dq[n][m] % 1000000007