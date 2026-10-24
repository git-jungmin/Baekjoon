import re
def solution(myStr):
    answer = []
    empty = True
    for i in re.split('[abc]',myStr):
        if i:
            empty = False
            answer.append(i)
    if empty == True:
        return ["EMPTY"]
    return answer