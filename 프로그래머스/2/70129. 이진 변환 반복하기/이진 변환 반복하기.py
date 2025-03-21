def solution(s):
    answer = [0, 0]
    while s != "1":
        s_len = len(s)
        s = "".join(s.split("0"))
        answer[1] += (s_len - len(s))
        answer[0] += 1
        s = format(len(s), 'b')
    return answer