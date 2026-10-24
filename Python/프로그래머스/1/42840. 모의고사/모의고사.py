def solution(answers):
    answer = []
    score = [0,0,0]
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    for i,v in enumerate(answers):
        if v == p1[i % 5]:
            score[0] += 1
        if v == p2[i % 8]:
            score[1] += 1
        if v == p3[i % 10]:
            score[2] += 1
    win = max(score)
    for i in range(3):
        if score[i] == win:
            answer.append(i+1)
    return answer