def solution(price, money, count):
    p = price
    for i in range(count):
        p = price * (i + 1)
        money -= p
    if money < 0:
        return -money
    else:
        return 0