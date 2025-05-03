def solution(n, wires):
    diff = []
    for i in range(0,len(wires)):
        w = wires[:i] + wires[i+1:]
        visited = set()
        for j in w:
            if not visited:
                visited.update([j[0],j[1]])
            for z in w:
                if z[0] in visited or z[1] in visited:
                    visited.update([z[0],z[1]])
        diff.append(abs(len(visited) - (n - len(visited))))
    return sorted(diff)[0]