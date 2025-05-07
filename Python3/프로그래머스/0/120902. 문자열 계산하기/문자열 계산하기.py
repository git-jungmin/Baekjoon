def solution(my_string):
    tokens = my_string.split(' ')
    answer = int(tokens[0])
    for i,v in enumerate(tokens):
        if v == '+':
            answer += int(tokens[i+1])
        elif v == '-':
            answer -= int(tokens[i+1])
    return answer