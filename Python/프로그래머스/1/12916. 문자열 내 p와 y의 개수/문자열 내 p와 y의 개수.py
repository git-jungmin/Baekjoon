def solution(s):
    answer = True
    count = 0
    for i in s:
        if i == 'p' or i == 'P':
            count+=1
        elif i == 'y' or i == 'Y':
            count-=1
    if count != 0:
        answer = False
    return answer