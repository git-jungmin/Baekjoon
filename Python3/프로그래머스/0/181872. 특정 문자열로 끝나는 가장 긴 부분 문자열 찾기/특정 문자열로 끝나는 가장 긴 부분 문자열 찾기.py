def solution(myString, pat):
    length = 0
    for i in range(0, len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            length = i
    return myString[:length + len(pat)]