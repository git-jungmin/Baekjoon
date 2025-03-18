def solution(nums):
    answer = 0
    num =  len(nums) // 2
    s = len(set(nums))
    if num <= s:
        answer = num
    else:
        answer = s
    return answer