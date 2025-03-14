from collections import deque
def solution(priorities, location):
    queue = deque([(priority, i) for i, priority in enumerate(priorities)])
    answer = 0
    while queue:
        first = queue.popleft()
        if any(first[0] < q[0] for q in queue):
            queue.append(first)
        else:
            answer += 1
            if first[1] == location:
                return answer
