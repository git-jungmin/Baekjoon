def solution(numbers):
    str_num = list(map(str, numbers))
    sort_num = sorted(str_num, key = lambda x : x * 3, reverse = True)
    answer = "".join(sort_num)
    if answer[0] == "0":
        answer = "0"
    return answer