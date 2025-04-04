def solution(arr1, arr2):
    len_diff = len(arr1) - len(arr2)
    if len_diff != 0:
        return 1 if len_diff > 0 else -1
    else:
        sum_diff = sum(arr1) - sum(arr2)
        if sum_diff != 0:
            return 1 if sum_diff > 0 else -1
        else:
            return 0