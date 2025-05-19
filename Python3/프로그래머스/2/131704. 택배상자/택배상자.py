def solution(order):
    truck = [] # 트럭
    container = [] # 보조 컨테이너
    head = 0
    for i in range(1,len(order)+1): # 들어오는 순서
        while container and order[head] == container[-1]:
            truck.append(container.pop())
            head += 1
        if order[head] == i:
            truck.append(i)
            head += 1
        else:
            container.append(i)
    while container and order[head] == container[-1]:
            truck.append(container.pop())
            head += 1
    return len(truck)