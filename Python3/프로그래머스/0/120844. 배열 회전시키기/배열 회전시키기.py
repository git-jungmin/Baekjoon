def solution(numbers, direction):
    if direction == 'right':
        num = numbers.pop(-1)
        numbers.insert(0,num)
    else:
        num = numbers.pop(0)
        numbers.append(num)
    return numbers