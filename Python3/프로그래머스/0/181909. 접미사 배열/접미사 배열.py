def solution(my_string):
    answer = []
    for i in range(len(my_string) - 1, -1, -1):
        answer.append(my_string[i:])
    return sorted(answer)