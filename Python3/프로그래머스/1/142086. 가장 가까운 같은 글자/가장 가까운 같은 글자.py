def solution(s):
    answer = [-1]
    s_array = list(s)
    for i in range(1,len(s)):
        answer.append(-1)
        for j in range(0,i):
            if s_array[j] == s_array[i]:
                answer[i] = i - j
    return answer