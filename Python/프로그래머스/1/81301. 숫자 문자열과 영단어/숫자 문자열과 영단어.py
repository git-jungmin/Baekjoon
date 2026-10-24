def solution(s):
    answer = ""
    dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    point = ""
    for i in s:
        if i.isdigit():
            answer += i
        else:
            point += i
        if point and point in dic:
            answer += dic[point]
            point = ""
    return int(answer)