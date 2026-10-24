def solution(a, b):
    i = a % 2
    j = b % 2
    if i == 0 and j == 0:
        return max(a,b) - min(a,b)
    elif (i == 0 and j != 0) or (i != 0 and j == 0):
        return 2 * (a + b)
    elif i != 0 and j != 0:
        return a**2 + b**2