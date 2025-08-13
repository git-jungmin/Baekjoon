def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:  # 짝수
            answer.append(i + 1)
        else: # 홀수
            b = '0' + bin(i)[2:]
            idx = b.rfind('0')
            b = list(b)
            b[idx] = '1'
            b[idx+1] = '0'
            answer.append(int(''.join(b),2))
    return answer