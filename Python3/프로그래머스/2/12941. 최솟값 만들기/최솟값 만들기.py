def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(0,len(A)):
        answer += A[i] * B[len(B) - i - 1]
    return answer