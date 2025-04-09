def solution(a, b, c):
    set_abc = set([a,b,c])
    i = a + b + c
    j = i * (a**2 + b**2 + c**2)
    z = j * (a**3 + b**3 + c**3)
    if len(set_abc) == 1:
        return z
    elif len(set_abc) == 2:
        return j
    else:
        return i