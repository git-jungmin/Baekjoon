def to_base_n(num, n):
    digits = "0123456789ABCDEF"
    if num == 0:
        return "0"
    result = ''
    while num > 0:
        result = digits[num % n] + result
        num //= n
    return result

def solution(n, t, m, p):
    answer = ''
    for i in range(t*m):
        answer += to_base_n(i,n)
    return answer[p-1::m][:t].upper()