from itertools import permutations
def solution(user_id, banned_id):
    def match(u,b):
        if len(u) != len(b):
            return False
        for i,j in zip(u,b):
            if j != '*' and i != j:
                return False
        return True
    answer = set()
    for p in permutations(user_id,len(banned_id)):
        if all(match(u,b) for u,b in zip(p,banned_id)):
            answer.add(tuple(sorted(p)))
    return len(answer)