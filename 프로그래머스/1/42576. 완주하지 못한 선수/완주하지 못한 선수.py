from collections import Counter
def solution(participant, completion):
    answer = ''
    counter = Counter(participant)
    for i in completion:
        counter[i] -= 1
    for j in counter:
        if counter[j] > 0:
            answer = j
    return answer