def solution(array, commands):
    answer = []
    for i in commands:
        sort_list = sorted(array[i[0] - 1 : i[1]])
        answer.append(sort_list[i[2] - 1])
    return answer