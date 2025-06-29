def solution(ingredient):
    answer = 0
    work = []
    for i in ingredient:
        work.append(i)
        if work[-4:] == [1,2,3,1]:
            answer += 1
            for j in range(4):
                work.pop()
    return answer