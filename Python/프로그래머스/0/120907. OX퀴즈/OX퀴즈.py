def solution(quiz):
    answer = []
    for i in quiz:
        X,op,Y,e,Z = i.split(" ")
        if op == "+":
            if int(X) + int(Y) == int(Z):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(X) - int(Y) == int(Z):
                answer.append("O")
            else:
                answer.append("X")
    return answer