def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            v = sum(arr1[i][z] * arr2[z][j] for z in range(len(arr1[0])))
            row.append(v)
        answer.append(row)
    return answer