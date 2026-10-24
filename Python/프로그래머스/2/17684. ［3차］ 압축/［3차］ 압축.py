def solution(msg):
    answer = []
    dic = {chr(i+64): i for i in range(1,27)}
    i = 0
    while i < len(msg):
        w = msg[i]
        j = i + 1
        while j <= len(msg) and msg[i:j] in dic:
            w = msg[i:j]
            j += 1
        answer.append(dic[w])
        if j <= len(msg):
            dic[msg[i:j]] = len(dic) + 1
        i = i + len(w)
    return answer