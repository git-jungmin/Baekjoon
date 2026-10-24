def solution(num_list, n):
    answer = []
    count = 0
    new_list = []
    for i in num_list:
        new_list.append(i)
        count += 1
        if count == n:
            count = 0
            answer.append(new_list)
            new_list = []
    return answer