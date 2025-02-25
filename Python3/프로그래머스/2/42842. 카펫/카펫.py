def solution(brown, yellow):
    answer = []
    for w in range(1, brown + yellow + 1):
        if (brown + yellow) % w == 0:
            h = (brown + yellow) // w
            if (w - 2) * (h - 2) == yellow:
                answer = [w, h]
    return answer