from collections import defaultdict
def solution(gems):
    answer = [0, len(gems)]
    shop = set(gems)
    left = 0
    find = defaultdict(int)
    
    for right in range(len(gems)):
        find[gems[right]] += 1
        
        while len(find) == len(shop):
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            
            find[gems[left]] -= 1
            
            if find[gems[left]] == 0:
                del find[gems[left]]
            
            left += 1
    
    return [answer[0]+1,answer[1]+1]