def solution(diffs, times, limit):
    def calc(lv):
        tot = 0
        
        for i in range(len(diffs)):
            t = times[i]
            d = diffs[i]
            
            if d > lv:
                tot += ((t + times[i-1]) * (d - lv))
            
            tot += t
            
            if tot > limit:
                return False
                          
        return True
        
    left = 1
    right = max(diffs)
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if calc(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer
        
        
        
        