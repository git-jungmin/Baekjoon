def solution(n):
    n_binary = format(n, 'b').count('1')
    while True:
        n += 1
        if format(n, 'b').count('1') == n_binary:
            return n