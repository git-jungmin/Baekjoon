from collections import deque
def solution(begin, target, words):
    answer = 0
    visited = set()
    queue = deque()
    queue.append((begin,0))
    while queue:
        current, step = queue.popleft()
        if current == target:
            return step
        for word in words:
            if word not in visited and match(word,current):
                visited.add(word)
                queue.append((word,step+1))
    return 0
def match(word1,word2):
    count = sum(c1 != c2 for c1,c2 in zip(word1,word2))
    return count == 1