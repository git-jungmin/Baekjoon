def solution(elements):
    s = set()
    for i in elements:
        for j in range(0, len(elements)):
            s.add(sum(elements[:j + 1]))
        n = elements.pop(0)
        elements.append(n)
    return len(s)