def solution(todo_list, finished):
    answer = []
    for t,f in zip(todo_list,finished):
        if f == 0:
            answer.append(t)
    return answer