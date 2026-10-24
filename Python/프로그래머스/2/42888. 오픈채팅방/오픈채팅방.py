def solution(record):
    answer = []
    user = {}
    for i in record:
        token = i.split(" ")
        if token[0] in ["Enter","Change"]:
            user[token[1]] = token[2]
    for j in record:
        action = j.split(" ")
        if action[0] == "Enter":
            answer.append(user[action[1]]+"님이 들어왔습니다.")
        elif action[0] == "Leave":
            answer.append(user[action[1]]+"님이 나갔습니다.")
    return answer