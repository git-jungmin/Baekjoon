def solution(numbers, k):
    nums = numbers*(k*2//len(numbers)+1)
    for i,v in enumerate(nums[::2]):
        if i+1 == k:
            return v