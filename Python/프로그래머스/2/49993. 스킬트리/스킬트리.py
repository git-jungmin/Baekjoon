def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        index = 0
        answer += 1
        for j in i:
            if j in skill:
                if skill[index] == j:
                    index += 1
                else:
                    answer -= 1
                    break
    return answer