def solution(n):
    answer = []
    for i in range(1,n*3):
        if len(answer) == n:
            break
        if i % 3 != 0 and "3" not in str(i):
            answer.append(i)
    return answer[-1]