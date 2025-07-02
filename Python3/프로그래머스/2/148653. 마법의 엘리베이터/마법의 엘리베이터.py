def solution(storey):
    answer = 0
    while storey > 0:
        n = storey % 10
        if n > 5:
            answer += (10-n)
            storey += 10
        elif n < 5:
            answer += n
        else:
            m = (storey // 10) % 10
            if m >= 5:
                answer += (10-n)
                storey += 10
            else:
                answer += n
        storey //= 10
    return answer