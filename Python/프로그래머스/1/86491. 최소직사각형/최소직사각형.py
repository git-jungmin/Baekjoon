def solution(sizes):
    size = list(map(lambda x : sorted(x), sizes))
    w, h = size[0][0], size[0][1];
    for i in range(1, len(size)):
        if size[i][0] > w:
            w = size[i][0]
        if size[i][1] > h:
            h = size[i][1]
    answer = w * h
    return answer