from collections import Counter
def solution(a, b, c, d):
    answer = 0
    nums = Counter([a,b,c,d])
    if len(nums) == 1:
        return 1111 * a
    elif len(nums) == 4:
        return min(nums)
    elif len(nums) == 2:
        if 3 in nums.values():
            p,q = 0,0
            for i,j in nums.items():
                if j == 3:
                    p = i
                if j == 1:
                    q = i
            return (10 * p + q)**2
        else:
            return max(nums)**2 - min(nums)**2
    else:
        mul = 1
        for i,j in nums.items():
            if j != 2:
                mul *= i
        return mul
    