def solution(phone_book):
    answer = True
    set_phone_book = set(phone_book)
    for i in phone_book:
        s = ""
        for j in i[:-1]:
            s += j
            if s in set_phone_book:
                answer = False
    return answer