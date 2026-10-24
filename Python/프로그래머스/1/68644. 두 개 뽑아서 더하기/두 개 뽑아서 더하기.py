def solution(numbers):
    answer = []
    numbers.sort()
    for i in range(0,len(numbers)):
        for j in range(i + 1, len(numbers)):
            k = numbers[i] + numbers[j]
            if k not in answer:
                answer.append(k)
    return sorted(answer)