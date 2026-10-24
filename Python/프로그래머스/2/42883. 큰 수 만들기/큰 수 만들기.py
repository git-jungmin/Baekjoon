def solution(number, k):
    stack = []
    for i in number:
        while k > 0 and stack and stack[-1] < i:
            k -= 1
            stack.pop(-1)
        stack.append(i)
    if k > 0:
        stack.pop(-1)
    return ''.join(stack)