def solution(numbers, target):
    answer = 0
    def DFS(index, tot):
        nonlocal answer
        if index == len(numbers):
            if tot == target:
                answer += 1
                return
        else:
            DFS(index + 1, tot + numbers[index])
            DFS(index + 1, tot - numbers[index])
    DFS(0,0)
    return answer