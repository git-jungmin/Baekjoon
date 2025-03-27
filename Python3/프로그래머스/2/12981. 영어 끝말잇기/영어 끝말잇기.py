import math
def solution(n, words):
    word_list = [words[0]]
    for i in range(1, len(words)):
        if word_list[-1][-1] != words[i][0] or words[i] in word_list:
            return [(i % n) + 1, math.ceil((i + 1) / n)]
        word_list.append(words[i])
    return [0,0]