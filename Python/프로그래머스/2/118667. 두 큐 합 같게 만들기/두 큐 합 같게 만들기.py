from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    a,b = sum(q1),sum(q2)
    target = (a + b) // 2
    limit = len(q1) * 3
    while a != target:
        if limit <= answer:
            return -1
        if a > b:
            n = q1.popleft()
            q2.append(n)
            a -= n
            b += n
        elif b > a:
            n = q2.popleft()
            q1.append(n)
            a += n
            b -= n
        answer += 1
    return answer