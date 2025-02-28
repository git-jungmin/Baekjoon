def solution(nums):
    answer = 0
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                tot = nums[i] + nums[j] + nums[k]
                p = True
                for r in range(2, tot // 2 + 1):
                    if tot % r == 0:
                        p = False
                        break
                if p:
                    answer += 1
    return answer