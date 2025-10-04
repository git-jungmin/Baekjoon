def solution(numbers):
    def to_binary(n):
        node = [1,3,7,15,31,63]
        n = bin(n)[2:]
        while len(n) not in node:
            n = '0' + n
        return n
    
    def binarytree(b):
        if len(b) == 1:
            return True
        root = len(b) // 2
        l,r = b[:root], b[root+1:]
        if b[root] == '0':
            return '1' not in l and '1' not in r
        else:
            return binarytree(l) and binarytree(r)
    
    answer = []
    for n in numbers:
        b = to_binary(n)
        answer.append(1 if binarytree(b) else 0)
    return answer