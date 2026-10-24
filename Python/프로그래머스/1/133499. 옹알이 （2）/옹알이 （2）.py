def solution(babbling):
    answer = 0
    speak = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        s = ''
        previous = ''
        p = False
        for j in b:
            s += j
            if s in speak:
                if s == previous:
                    p = True
                previous = s
                s = ''
        if not s and p == False:
            answer += 1
    return answer