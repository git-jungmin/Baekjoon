from collections import Counter
def solution(want, number, discount):
    answer = 0
    for i in range(0, len(discount) - sum(number) + 1):
        count = Counter(discount[i : i+10])
        match = True
        for w,n in zip(want,number):
            if count[w] != n:
                match = False
        if match == 1:
            answer += 1
    return answer