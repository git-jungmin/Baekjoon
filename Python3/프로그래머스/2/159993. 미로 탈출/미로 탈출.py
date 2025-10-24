def solution(maps): # DFS
    start,lever,exit = (0,0),(0,0),(0,0)
    for idx1,v1 in enumerate(maps):
        for idx2,v2 in enumerate(v1):
            if v2 == 'S':
                start = (idx1,idx2)
            elif v2 == 'L':
                lever = (idx1,idx2)
            elif v2 == 'E':
                exit = (idx1,idx2)
    def dist(s,e):
        visited = []
        stack = [[s,0]]
        while stack:
            (y,x),d = stack.pop(0)
            if (y,x) == e:
                return d
            if (y,x) not in visited:
                if (y-1) >= 0 and maps[y-1][x] != 'X' : # 위
                    stack.append([(y-1,x),d+1])
                if (y+1) < len(maps) and maps[y+1][x] != 'X' : # 아래
                    stack.append([(y+1,x),d+1])
                if (x+1) < len(maps[0]) and maps[y][x+1] != 'X' : # 우
                    stack.append([(y,x+1),d+1])
                if (x-1) >= 0 and maps[y][x-1] != 'X' : # 좌
                    stack.append([(y,x-1),d+1])
            visited.append((y,x))
    if dist(start,lever) and dist(lever,exit):
        return dist(start,lever) + dist(lever,exit)
    return -1