def solution(myString, pat):
    s = ''
    for i in myString:
        if i == 'A':
            s += 'B'
        elif i == 'B': 
            s += 'A'
    if pat in s:
        return 1
    else:
        return 0