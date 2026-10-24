from collections import deque
def solution(x, y, n):
    queue = deque([(x,0)])
    visited = set()
    while queue:
        current, count = queue.popleft()
        if current == y:
            return count
        if current < y and current not in visited:
            queue.append((current + n, count + 1))
            queue.append((current * 2, count + 1))
            queue.append((current * 3, count + 1))
        visited.add(current)
    return -1