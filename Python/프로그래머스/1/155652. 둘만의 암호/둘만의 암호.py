def solution(s, skip, index):
    answer = ''
    for i in s:
        count = 0
        c = ord(i)
        while count < index:
            c += 1
            if c > 122:
                c -= 26
            if chr(c) not in skip:
                count += 1
        answer += chr(c)
    return answer