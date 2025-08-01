import heapq
def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [-w for w in works]
    heapq.heapify(works)
    for i in range(n):
        num = heapq.heappop(works) + 1
        heapq.heappush(works, num)
    return sum(j**2 for j in works)