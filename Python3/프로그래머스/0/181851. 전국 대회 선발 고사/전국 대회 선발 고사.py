def solution(rank, attendance):
    att = []
    for i,v in enumerate(attendance):
        if v:
            att.append([rank[i],i])
    att.sort()
    return att[0][1] * 10000 + att[1][1] * 100 + att[2][1]