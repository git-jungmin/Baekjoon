def solution(s):
    answer = 0
    pair = {')': '(', ']': '[', '}': '{'}
    for _ in range(len(s)):
        stack = []
        is_valid = True
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack or stack.pop() != pair[ch]:
                    is_valid = False
                    break
        if is_valid and not stack:
            answer += 1
        s = s[1:] + s[0]
    return answer
