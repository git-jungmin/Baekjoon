def solution(sequence, k):
    answer = []
    left, right = 0,0
    total = sequence[0]
    while right < len(sequence):
        if total == k:
            if not answer or (right-left) < (answer[1] - answer[0]):
                answer = [left,right]
            total -= sequence[left]
            left += 1
        elif total < k:
            right += 1
            if right < len(sequence):
                total += sequence[right]
        else:
            total -= sequence[left]
            left += 1
    return answer