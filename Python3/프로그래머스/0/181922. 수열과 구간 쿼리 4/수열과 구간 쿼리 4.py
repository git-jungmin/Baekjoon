def solution(arr, queries):
    for i in queries:
        for j in range(0, len(arr)):
            if i[0] <= j <= i[1] and j % i[2] == 0:
                arr[j] += 1
                print(arr)
    return arr