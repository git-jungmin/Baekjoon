def solution(s):
    answer = ''
    s_list = s.split(" ")
    for i in s_list:
        if i:
            answer += i[0].upper() + i[1:].lower()
        answer += ' '
    return answer[:-1]