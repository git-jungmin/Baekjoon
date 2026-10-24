def solution(keymap, targets):
    answer = []
    for i in targets:
        tot = 0
        for j in i:
            nums = set()
            for key in keymap:
                for idx,v in enumerate(key):
                    if j == v:
                        nums.add(idx + 1)
            if not nums:
                tot = -1
                break
            tot += min(nums)
        answer.append(tot)
    return answer