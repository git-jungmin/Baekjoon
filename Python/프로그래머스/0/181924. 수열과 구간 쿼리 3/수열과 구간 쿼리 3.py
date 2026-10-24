def solution(arr, queries):
    for [i, j] in queries:
        i1 = arr[i]
        i2 = arr[j]
        arr[i] = i2
        arr[j] = i1
    return arr