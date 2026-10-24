def div(n):
    c = 0
    for _ in range(1,int((n+1)**(0.5)+1)):
        if n % _ == 0:
            c += 2
            if _ == (n // _):
                c -= 1
    return c
def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        count = div(i)
        if count > limit:
            answer += power
        else:
            answer += count
    return answer