def solution(arr):
    i = 0
    while len(arr) != 2**i:
        if len(arr) < 2**i:
            arr.append(0)
        else:
            i += 1
    return arr