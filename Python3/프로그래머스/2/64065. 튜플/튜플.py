def solution(s):
    answer = []
    result = []
    s = s[2:-2]
    for i in s.split('},{'):
        num = list(map(int, i.split(',')))
        result.append(num)
    result.sort(key = len)
    for j in result:
        for k in j:
            if k not in answer:
                answer.append(k)
    return answer