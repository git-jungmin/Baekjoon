from collections import Counter
def solution(s):
    answer = ''
    c = Counter(s)
    for i in c:
        if c[i] == 1:
            answer += i
    return ''.join(sorted(answer))