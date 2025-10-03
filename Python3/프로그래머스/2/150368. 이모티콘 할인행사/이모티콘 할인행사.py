from itertools import product
def solution(users, emoticons):
    answer = []
    discount = list(product([10,20,30,40], repeat = len(emoticons)))
    prices = [] # register, price
    for dc in discount:
        price = []
        register = 0
        for u in users:
            total = 0
            for idx,d in enumerate(dc):
                if u[0] <= d:
                    total += int((emoticons[idx] * (100-d)/100))
            if total >= u[1]:
                total = 0
                register += 1
            price.append(total)
        prices.append([register,sum(price)])
    prices.sort(reverse = True)
    return prices[0]