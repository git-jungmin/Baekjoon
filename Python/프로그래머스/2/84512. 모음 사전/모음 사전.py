def solution(word):
    answer = 0
    w = [781, 156, 31, 6, 1]
    a = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    for i, c in enumerate(word):
        answer += w[i] * a[c] + 1
    return answer