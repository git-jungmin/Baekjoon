def solution(lottos, win_nums):
    rank = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    high, low = 0,0
    for i in lottos:
        if i in win_nums:
            high += 1
            low += 1
        if i == 0:
            high += 1
    if low == 0:
        low += 1
    if high == 0:
        high += 1
    return [rank[high],rank[low]]