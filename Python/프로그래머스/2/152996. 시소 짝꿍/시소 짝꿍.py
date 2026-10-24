from collections import Counter
def solution(weights):
    answer = 0
    count = Counter(weights)
    for i in count:
        if count[i] >= 2:
            answer += ((count[i]*(count[i]-1))//2)
            print(answer)
    ratios = [1/2,2/3,3/4]
    for i in weights:
        for j in ratios:
            if (i * j) in count:
                answer += count[i * j]
    return answer