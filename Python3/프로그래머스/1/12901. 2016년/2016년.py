def solution(a, b):
    d = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    w = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    tot = b
    for i in range(1, a):
        tot += d[i]
        print(tot)
    return w[tot % 7]