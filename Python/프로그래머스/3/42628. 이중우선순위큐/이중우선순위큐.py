def solution(operations):
    queue = []
    for i in operations:
        if i[0] == 'I':
            queue.append(int(i[2:]))
        else:
            if queue and i[2:] == '-1':
                queue.remove(min(queue))
            elif queue and i[2:] == '1':
                queue.remove(max(queue))
    return [max(queue),min(queue)] if queue else [0,0]