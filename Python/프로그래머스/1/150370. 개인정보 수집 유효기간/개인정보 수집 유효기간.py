def solution(today, terms, privacies):
    answer = []
    term = {}
    today = today.split(".")
    today = int(today[0][2:]) * 28 * 12 + int(today[1]) * 28 + int(today[2])
    print(today)
    for t in terms:
        sep = t.split(" ")
        term[sep[0]] = int(sep[1])
    for index, privacie in enumerate(privacies):
        type = privacie[-1]
        p = privacie[0:10].split(".")
        day = (int(p[0][2:]) * 28 * 12 + int(p[1]) * 28 + int(p[2]) + term[type] * 28) - 1
        print(day)
        if today > day:
            answer.append(index + 1)
    return answer