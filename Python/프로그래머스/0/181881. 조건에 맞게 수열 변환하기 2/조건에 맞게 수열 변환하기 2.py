def solution(arr):
    count = 0
    before = arr[:]
    while True:
        after = before[:]
        for i in range(0,len(arr)):
            if after[i] >= 50 and after[i] % 2 ==0:
                after[i] /= 2
            elif after[i] < 50 and after[i] % 2 != 0:
                after[i] = after[i] * 2 + 1
        if before == after:
            return count
        count += 1
        before = after