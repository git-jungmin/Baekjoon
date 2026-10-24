import math
def solution(n,a,b):
    answer = 1
    while True:
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        if a != b:
            answer += 1
        else:
            return answer

