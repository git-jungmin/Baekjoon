def solution(dots):
    rec = sorted(dots)
    return (rec[2][0] - rec[0][0]) * (rec[1][1] - rec[0][1])