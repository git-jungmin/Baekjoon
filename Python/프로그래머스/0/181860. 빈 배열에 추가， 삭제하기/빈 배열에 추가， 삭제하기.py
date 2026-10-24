def solution(arr, flag):
    x = []
    for a, f in zip(arr, flag):
        if f == True:
            x.extend([a] * a * 2)
        else:
            x = x[:len(x) - a]
    return x