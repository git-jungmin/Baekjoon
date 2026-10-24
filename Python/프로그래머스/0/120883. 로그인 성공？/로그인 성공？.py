def solution(id_pw, db):
    answer = ''
    if id_pw in db:
        return "login"
    for i in db:
        if i[0] == id_pw[0]:
            return "wrong pw"
    return "fail"