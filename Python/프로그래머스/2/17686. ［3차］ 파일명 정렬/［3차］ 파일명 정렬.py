def sep(file):
    h,n,t = '','',''
    i = 0
    while i < len(file) and not file[i].isdigit():
        h += file[i]
        i += 1
    while i < len(file) and file[i].isdigit() and len(n) < 5:
        n += file[i]
        i += 1
    t = file[i:]
    return h,n,t

def solution(files):
    seperated = []
    for i in files:
        h,n,t = sep(i)
        seperated.append((h,n,t,i))
    seperated.sort(key = lambda x : (x[0].lower(), int(x[1])))
    return [j[3] for j in seperated]