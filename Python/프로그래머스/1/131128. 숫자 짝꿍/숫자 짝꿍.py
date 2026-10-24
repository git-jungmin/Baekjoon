from collections import Counter
def solution(X, Y):
    nums = list((Counter(X) & Counter(Y)).elements())
    if not nums:
        return '-1'
    else:
        string = ''.join(sorted(nums,reverse = True))
        if string[0] == '0':
            return '0'
        return string