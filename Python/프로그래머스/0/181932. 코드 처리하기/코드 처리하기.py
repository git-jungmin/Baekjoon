def solution(code):
    answer = ''
    mode = 0
    for i,v in enumerate(code):
        if mode == 0:
            if v != "1":
                if i % 2 == 0:
                    answer += v
            else:
                mode = 1
        else:
            if v != "1":
                if i % 2 != 0:
                    answer += v
            else:
                mode = 0
    if not answer:
        return "EMPTY"
    return answer