def solution(food):
    answer = []
    for i,v in enumerate(food):
        for j in range(0, int(v) // 2):
            answer.append(str(i))
    answer.append('0')
    for z in answer[len(answer)-2::-1]:
        answer.append(z)
    return ''.join(answer)