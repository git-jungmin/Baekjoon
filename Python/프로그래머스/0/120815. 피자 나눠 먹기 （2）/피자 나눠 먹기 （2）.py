import math
def solution(n):
    num = 1
    while True:
        if (num * 6) % n == 0:
            return num
        num += 1