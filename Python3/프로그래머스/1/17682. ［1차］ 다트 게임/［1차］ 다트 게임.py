def solution(dartResult):
    nums = []
    num = ''
    for i in dartResult:
        if i.isdigit():
            num += i
        elif i in 'SDT':
            if i == 'S':
                nums.append(int(num))
            elif i == 'D':
                nums.append(int(num)**2)
            elif i == 'T':
                nums.append(int(num)**3)
            num = ''
        elif i == '#':
            nums[-1] *= (-1)
        elif i == '*':
            nums[-1] *= 2
            if len(nums) >= 2:
                nums[-2] *= 2
    return sum(nums)