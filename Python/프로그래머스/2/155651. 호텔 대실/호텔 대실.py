import heapq
def solution(book_time):
    def to_min(t):
        h,m = map(int,t.split(':'))
        return h * 60 + m
    min_time = [(to_min(s),to_min(e)) for s,e in book_time]
    min_time.sort()
    heap = []
    for s,e in min_time:
        if heap and heap[0] <= s:
            heapq.heappop(heap)
        heapq.heappush(heap,e+10)
    return len(heap)