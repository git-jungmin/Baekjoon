def solution(my_string):
    answer = [0] * 52
    for i in my_string:
        if i.isupper():
            answer[ord(i)-ord('A')] += 1
        else:
            answer[26+ord(i)-ord('a')] += 1
    return answer