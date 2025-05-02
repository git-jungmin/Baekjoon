def solution(order):
    answer = 0
    for i in order:
        if 'americano' in i or i == 'anything':
            answer += 4500
        else:
            answer += 5000
    return answer