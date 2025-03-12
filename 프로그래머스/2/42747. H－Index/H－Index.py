def solution(citations):
    answer = 0
    for i in range(len(citations)):
        count = 0
        for j in range(0, len(citations)):
            if citations[j] > answer:
                count += 1
        print(count)
        if answer >= count:
            break
        answer += 1
    return answer