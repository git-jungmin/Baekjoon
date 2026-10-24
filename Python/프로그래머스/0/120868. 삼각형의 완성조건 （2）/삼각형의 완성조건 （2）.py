def solution(sides):
    answer = 0
    for i in range(1, max(sides)):
        if i + min(sides) > max(sides):
            answer += 1
    for j in range(max(sides), sum(sides)):
        answer += 1
    return answer