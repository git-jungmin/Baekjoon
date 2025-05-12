def solution(arr):
    max_len = max(len(arr),len(arr[0]))
    for row in arr:
        row.extend([0] * (max_len - len(row)))
    while len(arr) < max_len:
        arr.append([0] * max_len)
    return arr