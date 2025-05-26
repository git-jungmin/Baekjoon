from collections import Counter
def solution(array):
    count = Counter(array).most_common()
    if len(count) == 1 or count[0][1] != count[1][1]:
        return count[0][0]
    return -1