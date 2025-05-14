def divisor(num):
    nums = []
    for n in range(1,num+1):
        if num % n == 0:
            nums.append(n)
    return len(nums)

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        count = divisor(i)
        print(count)
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer