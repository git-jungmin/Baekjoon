from collections import deque
def solution(n, computers):
    answer = 1
    visited = set()
    queue = deque()
    queue.append(0)
    while queue:
        node = queue.popleft()
        for index,value in enumerate(computers[node]):
            if value == 1 and index not in visited:
                queue.append(index)
                visited.add(index)
        if not queue and len(visited) != len(computers):
            for i in range(0,len(computers)):
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
                    answer += 1
                    break
    return answer