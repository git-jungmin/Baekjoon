from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for i in permutations(dungeons):
        p = 0
        r = k
        for j in i:
            if j[0] <= r and j[1] <= r:
                r -= j[1]
                p += 1
        if p > answer: answer = p
    return answer