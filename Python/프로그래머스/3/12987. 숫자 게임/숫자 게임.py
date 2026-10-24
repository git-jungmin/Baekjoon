def solution(A, B):
    a,b = 0,0
    count = 0
    A,B = sorted(A), sorted(B)
    for i in range(len(A)):
        if A[a] < B[b]:
            count += 1
            a += 1
            b += 1
        else:
            b += 1
    return count