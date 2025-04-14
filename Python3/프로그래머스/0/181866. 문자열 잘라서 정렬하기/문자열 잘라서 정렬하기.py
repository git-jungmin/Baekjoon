def solution(myString):
    answer = sorted(filter(None, myString.split('x')))
    return answer