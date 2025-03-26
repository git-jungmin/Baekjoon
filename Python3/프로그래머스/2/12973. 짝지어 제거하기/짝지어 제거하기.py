def solution(s):
    stack = []
    for i in s:
        if stack and i == stack[-1]:
            stack.pop(-1)
        else:
            stack.append(i)
    return 1 if len(stack) == 0 else 0