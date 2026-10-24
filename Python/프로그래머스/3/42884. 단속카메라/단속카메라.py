def solution(routes):
    routes = sorted(routes, key = lambda x : x[1])
    camera = 0
    position = -30000
    for i in routes:
        if i[0] > position:
            camera += 1
            position = i[1]
    return camera
 