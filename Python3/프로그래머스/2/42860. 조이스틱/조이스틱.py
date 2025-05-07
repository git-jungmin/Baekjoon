def solution(name):
    answer = 0
    for i,v in enumerate(name):
        answer += min(ord(v)-ord('A'), 1+ord('Z')-ord(v))
        
    min_dis = len(name) - 1
    for i in range(len(name)):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        distance = i + len(name) - next + min(i, len(name) - next)
        min_dis = min(min_dis, distance)
    answer += min_dis
    return answer