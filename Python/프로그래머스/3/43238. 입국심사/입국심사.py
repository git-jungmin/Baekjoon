def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    
    while left <= right:
        count = 0
        mid = (left + right) // 2 #30
        
        for t in times:
            count += mid // t
        
        if count < n:
            left = mid + 1
        elif count >= n:
            right = mid - 1
            answer = mid
        
    return answer