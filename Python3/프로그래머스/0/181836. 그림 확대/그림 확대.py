def solution(picture, k):
    answer = []
    for i in picture:
        string = ''
        for j in i:
            string += (j * k)
        for _ in range(k):
            answer.append(string)
    return answer