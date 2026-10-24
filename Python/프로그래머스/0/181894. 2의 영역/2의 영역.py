def solution(arr):
    index_range = []
    for i,v in enumerate(arr):
        if v == 2:
            index_range.append(i)
    if index_range:
        return arr[index_range[0]:index_range[-1]+1]
    return [-1]