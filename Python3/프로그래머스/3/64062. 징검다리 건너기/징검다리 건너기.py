def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        count = 0
        
        for i in stones:
            if i - mid < 0:
                count += 1
            else:
                count = 0
            
            if count >= k:
                break
        
        if count >= k:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    
    return answer