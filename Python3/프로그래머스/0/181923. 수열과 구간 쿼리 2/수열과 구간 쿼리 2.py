def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        nums = []
        for i in arr[s:e+1]:
            if i > k:
                nums.append(i)
        if nums:
            answer.append(sorted(nums)[0])
        else:
            answer.append(-1)
    return answer