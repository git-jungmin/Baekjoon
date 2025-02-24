from collections import Counter

def solution(k, tangerine):
    answer = 0
    total = 0
    count = Counter(tangerine)
    sorted_tangerine = sorted(count.values(), reverse=True)
    for i in sorted_tangerine:
        total += i
        answer += 1
        if total >= k:
            break
    return answer