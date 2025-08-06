import math
def solution(n, stations, w):
    answer = 0
    head = 0
    section = w * 2 + 1
    for i in stations:
        answer += math.ceil((i-head-w-1)/section)
        head = i + w
    if head < n:
        answer += math.ceil((n-head)/section)
    return answer