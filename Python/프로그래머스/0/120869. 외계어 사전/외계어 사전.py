def solution(spell, dic):
    s = ''.join(sorted(spell))
    for i in dic:
        if ''.join(sorted(i)) == s:
            return 1
    return 2