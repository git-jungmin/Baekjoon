def solution(num_list):
    return max(sum(i for i in num_list[::2]),sum(i for i in num_list[1::2]))