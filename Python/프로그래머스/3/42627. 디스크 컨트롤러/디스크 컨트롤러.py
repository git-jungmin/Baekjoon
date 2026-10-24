import heapq
def solution(jobs):
    jobs.sort()
    heap = [] # (소요시간,요청시각,작업번호)
    time = 0 # 현재 시각
    total = 0
    idx = 0
    
    while heap or idx < len(jobs):
        
        while idx < len(jobs) and jobs[idx][0] <= time:
            ask, spend = jobs[idx]
            heapq.heappush(heap, (spend, ask, idx))
            idx += 1
        
        if not heap:
            time = jobs[idx][0]
            continue

        work = heapq.heappop(heap)
        time += work[0]
        total += (time - work[1])
    
    return total // len(jobs)